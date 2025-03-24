Overview
========
Apache Airflow is an open-source workflow orchestration tool used for scheduling and monitoring workflows, while Astronomer (often referred to as Astro) is a commercial platform built around Apache Airflow.
Astro airflow is derived from Apache Air flow. This project was generated after 'astro dev init' using the Astronomer CLI. This readme describes the contents of the project, as well as how to run Apache Airflow on your local machine.


Prometheus and Grafana:

To track request rate/response time. We can use to obtain load/public usage or For Alerts and Notifications:
Alerting: Prometheus can trigger alerts based on predefined thresholds or anomaly detection. For example, you might set an alert after usage of endpoint is high/more no of users or if the response time for an API exceeds a certain limit or if the CPU usage goes beyond a threshold.

These two cant be dierctly installed on Windows/Mac, we will use docker file and containarize them
docker-compose.yml
services:
  prometheus:    
    image: prom/prometheus:latest
    container_name: prometheus
    ports:
      - "9090:9090"
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml
    networks:
      - monitoring

  grafana:
    image: grafana/grafana:latest
    container_name: grafana
    ports:
      - "3000:3000"
      
Project Contents
================

Your Astro project contains the following files and folders:

- dags: This folder contains the Python files for Airflow DAGs. (example https://www.astronomer.io/docs/learn/get-started-with-airflow).
- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. 
- include: This folder contains any additional files 
- requirements.txt: Install Python packages needed for project by adding them to this file. 
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as develop DAGs in this project.

Deploy Project Locally
===========================



1. Start Airflow on local machine by running 'astro dev start'.

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

2. Verify that all 4 Docker containers were created by running 'docker ps'.

Note: Running 'astro dev start' will start  project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432. If you already have either of those ports allocated, you can either [stop your existing Docker containers or change the port](https://www.astronomer.io/docs/astro/cli/troubleshoot-locally#ports-are-not-available-for-my-local-airflow-webserver).

3. Access the Airflow UI for your local Airflow project. To do so, go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.

You should also be able to access your Postgres Database at 'localhost:5432/postgres'.

Deploy Project to Astronomer
=================================

Steps :
1. Astro Airflow: 
Astro airflow CLI install - https://www.astronomer.io/docs/astro/cli/get-started-cli/
astro dev init
astro dev start
  dockerfile for airflow will build and install apache google providers as well

3. pip install -e .
4. Get GCP Key --------------------------------------
GCP bucket service account creation IAM->Service account

5. ETL Pipeline making
   - Extract step-Read Data from GCP bukcet 
   - Transform step- from CSV -> pandas dataframe ->SQL database
   - Load into SQL database using python operator and psycopg2 connection ->[PostGreSQL]

6. Endpoint connection building
   Apache airflow dashboard
   EP1- GCP bucket
   EP2-Postgres database
   http://localhost:8080/connection/list/
   
   Dbeaver app[@port 5432] can be used to check database is correct or not
   Becuase SQL databsae is running on docker container not on local PC
   
     
4. INSTALL REDIS --------------------------------------
docker pull redis
docker run -d --name redis-container -p 6379:6379 redis


ML MONITORING ---------------------------------------
Prometheus + Grefana

DOCKER-COMPOSE.YAML
docker-compose up -d

