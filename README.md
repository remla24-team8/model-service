# model-service

The model-service represents a wrapper service for the released ML model. It offers a REST API to exposes the model to other components and make it scalable.

`http://host_ip/` offers a small introduction of the endpoint


## Usage

### Development setup

Set up Poetry using Python 3.12 (i.e. use `poetry env use <python 3.12 executable here>`).

Install dependencies and the project using `poetry install`

Run the service using `poetry run flask --app model_service.app run`.

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