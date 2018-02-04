# Comparing Cryptocurrency prices with Reddit Data

## Motivation

In order to learn more about Celery, Redis, and MongoDB, I started this project.  It is an application that pulls data about the market capitalization of the top cryptocurrencies and compares that with the current sentiment of Reddit comments.  It tests whether you can tell anything about the movement of prices based on the mood of Reddit's users.  

## Project Status

Much of the backend architecture is complete - I currently have docker containers for Celery workers, a Redis instance that serves as a message broker, and a connection to a Mongo container as a data store.  The logic for pulling Reddit and Crypto data is complete.  

## Next Steps

The next step is incorporating a cronjob container that can communicate with the other containers and schedule jobs.  After that, I need to finalize the way I store data in Mongo, and then attach a chart on the frontend.  Additionally, a script on the frontend will need to pull data every 5 minutes to update the chart.  

## Installation

You will need a Docker engine in order to download this project.  I will also be hosting the image on DockerHub - TODO Link here

bash
```
docker-compose up
```

## Technical Hurdles

## Looking Back

## Future Features
