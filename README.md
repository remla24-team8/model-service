# model-service

The model-service represents a wrapper service for the released ML model. It will offer a REST API to exposes the model to other components and make it scalable.

• Fetch the pre-trained ML model and setup the environment to make it queryable.(An excellent solution will find ways to avoid including the model in the image.)

• Depends on the lib-ml through a package manager (e.g., PyPi) to pre-processing queries.

• Embed the ML model in a Flask webservice, so it can be queried via REST.

• A workflow is used to automatically release the library in the GitHub container registry.

• The container is versioned automatically, e.g., by picking-up on the corresponding Git version tag.