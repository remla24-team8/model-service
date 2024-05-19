# model-service

The model-service represents a wrapper service for the released ML model. It offers a REST API to exposes the model to other components and make it scalable.

`http://host_ip/` offers a small introduction of the endpoint


## Usage

### Development setup

Install `uv`.

Install dependencies and the project using `uv pip sync requirements.txt`.

Enter the venv using `. .venv/bin/activate` (or similar for your platform/shell).

Go into the `src` directory.

Run the service using `flask --app model_service.app run`.

### Production usage
When the endpoint has been setup, make a POST request to `http://host_ip/predict`, following the data format:
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
