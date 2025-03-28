# <img src="src/app/static/globe.png" alt="" width="20"> PROJECT ORION

_Observation, Reconnaissance, Intelligence, and Operations Network_

[![Version](https://img.shields.io/github/v/release/IsaiahHarvi/ORION.svg)](https://github.com/IsaiahHarvi/ORION/releases)
[![Tests Passing](https://img.shields.io/github/actions/workflow/status/IsaiahHarvi/ORION/integration.yml)](https://github.com/IsaiahHarvi/ORION/actions?query=workflow%3Atest)
[![GitHub Contributors](https://img.shields.io/github/contributors/IsaiahHarvi/ORION.svg)](https://github.com/IsaiahHarvi/ORION/graphs/contributors)
[![Issues](https://img.shields.io/github/issues/IsaiahHarvi/ORION.svg)](https://github.com/IsaiahHarvi/ORION/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/IsaiahHarvi/ORION.svg)](https://github.com/IsaiahHarvi/ORION/pulls)

---

A versatile software platform designed for use across missions in public safety, security, environmental monitoring, and defense. Leveraging machine learning, ORION filters and transforms data from diverse sources—including UAVs and NEXRAD—into actionable insights for effective decision-making.

**A presentation is available [here](docs/PROJECT_ORION.pdf)**

### <a>Production Version<a href = "https://orion.harville.dev/"></a>

---

A production version of this project is available at [orion.harville.dev](https://orion.harville.dev/).

## Development Version

Interested users can build the project themselves.

1. **Start the Project:**

    Open your terminal in the project directory and start the Docker containers.

    ```bash
    git clone --recurse-submodules git@github.com:IsaiahHarvi/ORION.git
    cd ORION
    docker compose --profile gui up --build
    # Optionally, to target the developmentAPI rather than a locally hosted API export the following env var
    export VITE_API_URL=http://localhost:5171
    ```

2. **Access the Application:**

    Once the containers are running, open your browser and navigate to:

    ```
    http://localhost:5173
    or
    http://127.0.0.1:5173
    ```

    This will load your project locally.

### Additional Information

-   **Stopping the Containers:**
    To stop the running containers, press `Ctrl+C` in the terminal and then run:

    ```bash
    docker compose --profile gui down
    ```

----

## API
Our API is available at: https://orion.harville.dev/api/docs


## [LICENSE](./LICENSE)
