# API Authentication and Authorization with JWT - Web Security Introduction - The Basics

Name:

UCID:

## Introduction

In this unit, you will be introduced to some basic concepts in web application security. You will learn about
authentication and authorization as well as learn about the supporting technology of HTTPS that secures the
communication between a web client and server. You will see how to store user passwords using hashing and understand the
different hashing algorithms. You will also learn the difference between encryption and hashing. In this project I am
providing you the complete user registration and login process as well as a demonstration of how to protect a route.

You must watch the video and read the reading in order to prepare yourself for project 2. I am not requiring you to do
anything with the code at this time; however, you should experiment with it and carefully review it, so that you can
implement it from scratch for your final project and properly test it. All you need to do is submit a link to the
repository back to campuse, so I know you accepted the assignment and hopefully went over all the material for the unit.

If you want to challenge yourself, you should implement this:

https://flask-jwt-extended.readthedocs.io/en/stable/blocklist_and_token_revoking/  <-Adds logout essentially

and

https://flask-jwt-extended.readthedocs.io/en/stable/refreshing_tokens/   <- Adds the ability to refresh expired tokens

You will need to implement this for your project, so I would get started on trying to do it now and test it!

* Note: This unit is focused only on this topic and does not include swagger, or JSONAPI, so that we can look at the
  fundamental concepts of security. We will be improving security and adding Swagger and JSONAPI spec back to the
  project over the next few lessons. Your final project will be to design and deploy a secure API that includes
  all the functionality that we have covered up until this point in the course.

### Unit Videos

[Watch this](https://youtu.be/B8UzrzECZzs)

### Required Readings

1. [Good Example Code I used](https://github.com/picsouds/flask-smorest-example-bookmanager)
## Put a link to your Production Heroku Deployment Here

* [Production Deployment]()

## Instructions To Deploy To Heroku and Submit the Assignment

1. Clone this repo to your local
2. Submit a link to your assignment repository to Canvas

## Running Locally

1. To Build with docker compose:
   docker compose up --build
2. To run tests, Lint, and Coverage report use this command: pytest --pylint --cov

.pylintrc is the config for pylint, .coveragerc is the config for coverage and setup.py is a config file for pytest

### Future Notes and Resources
