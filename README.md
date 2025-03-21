# Kubernetes Minikube Cluster with Elasticsearch, Kibana, MySQL, and Custom API

## Overview 📝

This project demonstrates the integration of **Elasticsearch** and **MySQL** within a **Kubernetes Minikube** cluster. The primary goal is to transfer data in real-time from MySQL to Elasticsearch using a **custom Python API**. The architecture includes:
- **Elasticsearch** for scalable search and analytics.
- **MySQL** as the relational database storing student data.
- A **custom Python API** that fetches data from MySQL and pushes it to Elasticsearch, simulating a real-time data streaming scenario.

## Why a Custom API Instead of Logstash? 🤔

We considered Logstash for real-time data streaming but faced challenges with:
- **High resource consumption**: Logstash was too demanding on our machine.
- **Networking setup**: Difficulties in configuring Logstash to connect with MySQL with JDBC.

Opting for a **custom Python API** allowed us to:
- **Reduce resource usage**
- **Improve control and flexibility**

## Setup

### 1. Minikube Setup 🚀
Start Minikube:
```sh
minikube start
```

### 2. Deploy Elasticsearch & Kibana 🕵️‍♂️
Deploy Elasticsearch and Kibana:
```sh
kubectl apply -f k8s/elasticsearch.yaml
kubectl apply -f k8s/kibana.yaml
```

### 3. MySQL Database Setup 🗃️
Set up MySQL and initialize with data:
```sh
kubectl apply -f k8s/mysql-deployment.yaml
```

### 4. Custom Python API 🐍
Build and deploy the Python API container:
```sh
eval $(minikube docker-env)

PASSWORD=$(kubectl get secret quickstart-es-elastic-user -o go-template='{{.data.elastic | base64decode}}')
docker build --build-arg PASSWORD=$(echo $PASSWORD) -t send_py api

kubectl apply -f k8s/python-api.yaml
```

## Usage

Once deployed, the Python API will:
1. Connect to MySQL 🖧
2. Fetch data and send it to Elasticsearch 🔄
3. Insert random data into MySQL for real-time simulation ⏱️

You can monitor data in Kibana via Minikube dashboard:
```sh
minikube dashboard &
```
