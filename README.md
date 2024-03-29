# rob_onboarding

rob onboarding project


## Developing

To setup the project for local development, make sure you have a virtualenv setup, and then run:

    pip install -e .

This will install all the dependencies and set the project up for local usage.


## Postgres

The service requires a Postgres user and two datbases (one is for testing):

    createuser rob_onboarding
    createdb -O rob_onboarding rob_onboarding_db
    createdb -O rob_onboarding rob_onboarding_test_db

The service schema can be initialized using:

    createall [-D]


## Flask

To run the Flask web server when developing locally, invoke the following:

    runserver

The service publishes several endpoints by default.

 -  The service publishes its own health:

        GET /api/health

 -  The service publishes a [crawlable](https://en.wikipedia.org/wiki/HATEOAS) endpoint for discovery
    of its operations:

        GET /api/

 -  The service publishes [Swagger](http://swagger.io/) definitions for its operations (by API version)
    using [HAL JSON](http://stateless.co/hal_specification.html):

        GET /api/v1/swagger
