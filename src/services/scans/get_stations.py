from math import atan2, cos, radians, sin, sqrt

import pandas as pd
from geopy.geocoders import Nominatim


def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate distance between two points (in km) using the Haversine formula."""
    R = 6371.0  # Earth's radius in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


def get_radars(target_lat, target_lon, radius_km=100, output_format="list"):
    station_df = pd.read_csv("data/nexrad_stations.csv")
    station_df["distance_km"] = station_df.apply(
        lambda row: haversine_distance(
            target_lat, target_lon, row["Latitude"], row["Longitude"]
        ),
        axis=1,
    )
    nearby_radars = station_df[station_df["distance_km"] <= radius_km].sort_values(
        "distance_km"
    )

    if output_format == "list":
        return nearby_radars["Radar ID"].tolist()
    elif output_format == "json":
        json_df = nearby_radars[
            ["Radar ID", "Latitude", "Longitude", "distance_km"]
        ].rename(
            columns={
                "Radar ID": "radar_id",
                "Latitude": "lat",
                "Longitude": "lon",
                "distance_km": "distance",
            }
        )
        return json_df.to_dict(orient="records")
    elif output_format == "readable":
        return nearby_radars[
            ["Radar ID", "Latitude", "Longitude", "distance_km"]
        ].to_string(index=False)
    else:
        raise ValueError(
            "Invalid output_format. Expected 'list', 'json', or 'readable'"
        )


if __name__ == "__main__":
    city = input("Enter a city (or leave blank to input lat/lon): ").strip()
    if city:
        geolocator = Nominatim(user_agent="nexrad_locator")
        location = geolocator.geocode(city)
        if location is None:
            print(f"Could not geocode '{city}'. Please check the city name.")
            exit(1)
        target_lat = location.latitude
        target_lon = location.longitude
        print(f"Coordinates for {city}: {target_lat}, {target_lon}")
    else:
        try:
            target_lat = float(input("Enter latitude: "))
            target_lon = float(input("Enter longitude: "))
        except ValueError:
            print("Invalid coordinate input.")
            exit(1)

    radius_km = 200
    nearby_radars = get_radars(target_lat, target_lon, radius_km)
    if nearby_radars.empty:
        print(f"No radars found within {radius_km} km of the provided location.")
    else:
        print("Nearby Radars:")
        print(nearby_radars[["Radar ID", "Site Name", "distance_km"]])
