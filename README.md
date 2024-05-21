# model-service

The model-service represents a wrapper service for the released ML model. It offers a REST API to exposes the model to other components and make it scalable.

## Usage

### Development setup

Install `uv`.

If the dependencies are not up to date, run first `uv pip compile pyproject.toml -o requirements.txt`.

Install dependencies and the project using `uv pip sync requirements.txt`.

Enter the venv using `. .venv/bin/activate` (or similar for your platform/shell).

Go into the `src` directory.

Run the service using `flask --app model_service.app run`.

### Production usage

The model is built using GitHub Actions as an image, which can be found here: https://github.com/remla24-team8/model-service/pkgs/container/model-service. The port used is 5000.

See the operation repo for setup in Docker Compose.

### Making requests
When the endpoint has been setup, make a POST request to `http://<host>/predict`, following the data format:
```
{
    "url": ['example1.com', 'example2.com']
}
```
or
```
{
    "url": 'example1.com'
}
```
It will return a list of prediction scores.
