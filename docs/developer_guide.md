# Raspberry PI System Monitor API

## Introduction
Raspberry Pi System Monitor API is a RESTful web service that exposes system information from a Raspberry Pi through a JSON-based API. Built with Python and FastAPI, it provides access to processor, memory, disk, operating system, network, and hardware information for use by monitoring applications, automation scripts, dashboards, or other software.  

The project demonstrates a common pattern used in modern API development: collecting data from multiple sources, organizing it into a consistent data model, and exposing it through a documented REST interface. Interactive API reference documentation is generated automatically from the application's OpenAPI specification, while this guide explains how the project is organized, how to run it, and how to use the API effectively.  

Although this project is intentionally small, the design principles are the same ones used in larger production APIs. The guide therefore serves both as documentation for the software and as an introduction to the concepts behind API design and developer documentation.

## Prerequisites
Before installing and running the Raspberry Pi System Monitor API, ensure the following requirements are met:
### Hardware
* Raspberry Pi 4 Model B or another compatible Raspberry Pi capable of running the supported operating system.

### Software
* Python 3.13.or later
* pip package installer
* Git (for cloning the repository)

### Development Environment
* A Python virtual environment (venv) is recommended to isolate project dependencies from the system Python installation.

### Network
* Network connectivity between the Raspberry Pi and any client devices that will access the API.

## Installation
Follow these steps to install the Raspberry Pi System Monitor API on a Raspberry Pi or another supported Linux system.
1. Clone the repository.  
Clone the project from GitHub and change to the project directory.
`git clone https://github.com/<username>/rpi-system-monitor.git`
`cd rpi-system-monitor`
2. Create a Python virtual environment to isolate the project's dependencies.  
`python3 -m venv .venv`
3. Activate the virtual environment.  
Activate the virtual environment before installing any packages.  
`source .venv/bin/activate`  
If activation is successful, your prompt will bein with (.venv).
4. Install project dependencies.
Install the required Python packages listed in the file requirements.txt.
`pip install -r requirements.txt`
5. Verify the required packages are available by running the following command:
`pip list`
  
The project is now installed and ready to run.

## Starting the API
Start the API server from the project's root directory while the virtual environment is active:
`uvicorn api:app --host 0.0.0.0 --port 8000`
Leave the terninal window open while the API is running.

## Accessing the API
Once the server is running, you can access it from a web browser or an HTTP client.
URL     Purpose
http://localhost:8000/docs  Interactive Swagger UI
http://localhost:8000/openapi.json  OpenAPI specification

Note: If the Raspberry Pi is accessed from another computer on the same network, replace `localhost` with the Raspberry Pi's hostname or IP address.

## Exploring the API with the Swagger UI

### Introduction
FastAPI automatically generates interactive API documentation from the application's OpenAPI specification. This documentation is presented through Swagger UI, allowing developers to explore the API directly from a web browser.  

Unlike a static reference manual, Swagger UI is interactive. You can inspect endpoints, view request and response schemas, execute requests, and examine the JSON returned by the server without writing any client code.  

Open the following URL in your browser:
http://localhost:8000/docs  

If you are accessing the API from another device on the same network, replace localhost with the Raspberry Pi's hostname or IP address.

### Understanding the Swagger UI
Swagger organizes the API into several sections.

#### Endpoints

**Executing a request**
To test an endpoint using the Swagger UI:
1. Click an endpoint, such as GET/system.
2. Click Try it out.
3. Click Execute.  

Swagger will display the following:
* The HTTP request that was sent.
* The equivalent `curl` command.
* The HTTP status code.
* The JSON response body.

#### Schemas

Near the bottom of the page, Swagger displays a section named Schemas.  

A schema describes the structure of the data returned by the API. Rather than showing actual values, it defines the fields that appear in a request or response and the type of data each field contains.  

For example, a simplified schema might look like this:  
Field       Type
hostname    string
cpu_usage   number
memory_usage    number
disk_usage  number

#### OpenAPI Specification
Swagger UI is generated automatically from the API's OpenAPI specification, which is available at:
http://localhost:8000/openapi.json. 

The OpenAPI document is a machine-readable description of the API. Development tools can use it to generate client libraries, validate requests and responses, or produce alternative documentation formats.

## Endpoint Summary

## Sample Workflow

## Project Structure

## Future Enhancements