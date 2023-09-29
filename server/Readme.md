# RentEZ - Server

### Tech used

[![Python](https://img.shields.io/badge/python-blue?style=for-the-badge&logo=python&logoColor=yellow)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/fastapi-teal?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/mongodb-darkgreen?style=for-the-badge&logo=mongodb&logoColor=white)]()

## Pre-requisites
[**Python**](https://www.python.org/downloads/)

## How to build/run locally

1. Clone the repository to your machine.
2. Fill in `.env` with the required information.
3. Run the following command to install the requirements in the terminal of your ide in the `/RentEZ` path:
    ```shell
    pip install pipenv
    cd backend/
    mkdir venv && cd venv
    pipenv shell
    pipenv install -r reuirements.txt
    pip install -r requirements.txt
    ```
4. After the required files are installed, in the `/backend` path run:
    ```
    uvicorn main:app --reload
    ```
5. The project will be up and running in your machine. In any browser type `http://localhost:8000/docs` to get the `docs` of the project.

    *Note -* The `/docs` route is provided by default by FastAPI with the help of `Swagger UI`. Get to know more about Swagger UI [here](https://github.com/swagger-api/swagger-ui).

7. To close the server press `Ctrl+C` or `Cmd+C` in the terminal.

6. To close the running environment shell type `exit` in the terminal and press enter.