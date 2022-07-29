[![Production Workflow 1](https://github.com/kaw393939/jwt-web-security-part-2/actions/workflows/prod.yml/badge.svg)](https://github.com/kaw393939/jwt-web-security-part-2/actions/workflows/prod.yml)

# Project 2

Name:

UCID:

## Introduction

This is the final unit for the course and brings together a lot of concepts we have seen throughout the course to make a
reasonably secure professional API. Because we are almost at the end of the semester, and I want you to have time to do
your final project, I am combining this lesson with the final project. You have some requirements to complete for the
unit and options to complete for your final project. You just need to select two options, or you can ask me to approve
another idea; however, it must be done with this repository no exceptions.

Note: When you run the app you have to go to <host>:port/swagger-ui

### Unit Videos

[Watch this](https://youtu.be/Yt-0BWdauaI)

### Required Readings

1. [Good Example Code I used](https://github.com/picsouds/flask-smorest-example-bookmanager)
2. [smorest - The main libray I used for swagger](https://flask-smorest.readthedocs.io/en/latest/)
3. [CORS Explained](https://medium.com/@baphemot/understanding-cors-18ad6b478e2b)
4. [Marshmallow Explained](https://www.kimsereylam.com/python/2019/10/25/serialization-with-marshmallow.html)

### Optional Readings - Required if you don't know SQLALchemy 
1. [Help with SQL Alchemy, similar but not exactly how we do it](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
2. [More or less exactly the queries you need and the code to do it](https://www.golinuxcloud.com/flask-sqlalchemy/)
3. [SQL Alchemy RElationships](https://hackersandslackers.com/sqlalchemy-data-models/)
### Project Requirements: (20 Points Each) 3 x 20 = 60

1. You must finish the patch/put (model update) and delete methods along with the swagger spec for cities and countries.
2. You must write tests for successful requests and error responses for item #1.
3. You must fix all the pylint problems by resolving the issue or disabling where appropriate

**Note** Put all the tests for this in [test_geography_project2.py](tests/test_geography_project2.py)

### Project Options (Pick 2): (20 Points Each)  2 x 20 = 40

1. Implement the token refresh for JWT as described in the previous unit, you will need to write tests for this
2. Implement the token blacklist functionality with testing as described in the previous unit.
3. Implement and test the pagination functionality i.e. breaking down a list of records into separate pages as described
   here [Smorset Pager](https://flask-smorest.readthedocs.io/en/latest/pagination.html). You will need to write tests to
   prove the pager works and research this feature.
4. You can add a new blueprint for your own data, but don't remove geography, so that the geography tests pass
5. You can try to implement Hypermedia as the Engine of Application State (HATEOAS) on the response object by changing
   the schema to use flask [marshmellow jsonAPI](https://marshmallow-jsonapi.readthedocs.io/en/latest/)
6. Add Alembic Migrations

**Total Points:  60 + 40 = 100**

**Note On Submission** Put the tests for the two options you select
in [test_option_you_pick_one.py](tests/test_option_you_pick_one.py)
and [test_option_you_pick_two.py](tests/test_option_you_pick_two.py)

**Note On Option 4**: I played around with #4; however it was a lot of code, so I just didn't do it now. The trick is to
use a
different schema for the response that comes marshmello jsonAPI (it won't work for incoming post requests without a lot
of work and figuring out some errors). If you want to do this, you should message me, and I will tell you what I figured
out. WHat I realized was that implementing this would make the code more confusing, until
you understood more of what marshmallow is doing. We did this before and you might be able to partially reuse the schema
from SAFRS in project 1.

## Submission Requirements

1. Your API must be available on Heroku as with previous assignments. Refer to the instructions on previous assignments.
2. You must submit a link to the repository on Canvas
3. You must put a Github Actions Badge on the assignment at the very top.
4. You must put a link to the swagger UI page below

## Put a link to your Production Heroku Deployment Here

* [Swagger UI Link On Heroku](https://kwilliam-prod.herokuapp.com/swagger-ui)

## Running The app

### Running Locally - On my Mac this works locally just fine; however, I think windows might need to run it in Docker.

1. Flask Run <- Runs the app
2. Flask routes <- SHows routes
3. pytest --pylint <- run tests and lint

### Running with Docker - Login to the container to run tests

1. docker ps <- lists running containers
2. docker kill <container id>  kills the container, you get the container ID from docker PS
    * Example: docker kill cf373e38ae66
3. docker compose up --build <- builds the app locally
4. docker exec -it <containerID> /bin/bash    <- Logs into the running container
    * Example: docker exec -it cf373e38ae66 /bin/bash
