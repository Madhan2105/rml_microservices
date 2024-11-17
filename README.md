# Microservices Publisher, Consumer, and API

## Overview

This project consists of three microservices: **Publisher**, **Consumer**, and **API**, implemented using Python, Flask, RabbitMQ, and PostgreSQL. The services are containerized using Docker and managed via Docker Compose.

### Architecture

- **Publisher Service**: Reads data from a file and publishes tasks to RabbitMQ.
- **Consumer Service**: Consumes tasks from RabbitMQ and stores them in PostgreSQL.
- **API Service**: Provides an API to fetch data from PostgreSQL with filtering, searching, and pagination capabilities.

The services are connected via RabbitMQ for message brokering and PostgreSQL for data persistence.

---

## Components

### Publisher Service
- Reads a file line by line and publishes each line as a task to RabbitMQ.

### Consumer Service
- Consumes tasks from RabbitMQ and stores them in PostgreSQL.

### API Service
- Provides API endpoints for querying and managing records in PostgreSQL.
- Supports **searching**, **filtering**, and **pagination**.

### RabbitMQ
- Message broker used to queue tasks from the Publisher service to the Consumer service.

### PostgreSQL
- Database for storing the records consumed by the Consumer service.

---

## Project Setup

### Prerequisites

- Python 3.9+
- Docker and Docker Compose
- PostgreSQL

### Clone the Repository

```bash
git clone <repository_url>
cd <repository_folder>

### Build and Start Services
