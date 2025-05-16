# 🚀 Zip Code API - Code Sample Repository
---
## Overview

The US Zip Code API, which encompasses multiple endpoints, supplies an enhanced JSON-formatted data model for United States zip code information. Employing REST design principles, this versatile API enables you to integrate essential functionalities like zip code validations, city searches, distance calculations, radius searches, and more into your applications. 

## 🛠 Content

This repository contains easy-to-use sample code that can help demonstrate functionality from the [**Zip Code API**](https://www.metadapi.com/API-Products/Zip-Code-API). Each sample is designed for **simplicity** and **ease of integration**. Just plug in your **API key**, and you're good to go! To get an API Key mivist the [Zip Code API](https://www.metadapi.com/API-Products/Zip-Code-API) home page and subscribe to any of the available subscription tiers.

Zip Code API has the following endpoints:

- **Get Zip Code**. This end point takes the 5 digit zip code in the endpoint path and returns all details for that zip code.
- **List All Zip Codes**. Returns a list of zip codes. Includes 16 query string parameters that can help you filter your search criteria.
- **Distance Between 2 Zip Codes**. Gets the distance (in miles and kilometers) between 2 zip codes passed as parameters. There are 2 mandatory query parameters (zipCode1 and zipCode2).
- **Zip Code Radius**. Endpoint that returns the zip codes that fall within the specified radius of another zip code. The returned zip codes are sorted by distance.
- **List all MSA Groups**. This end point lists all the Metropolitan and Micropolitan Statistical Areas in the United States with the corresponding states and counties that make up the group.
- **MSA Details**. Gets the details of a single Metropolitan Statistical Area code passed as a path parameter.
- **IRS Statistics of Income**. Detailed IRS statistics of income by zip code.
- **Validate key**. Endpoint used to validate license key only. Returns 204 on Success. Simple way to test connection or ping zip code service. 

## 🔥 Why Use This API?
The **Zip Code API** gives you instant access to essential location data, including:
- ✅ **Zip code lookups**
- ✅ **City & state information**
- ✅ **Latitude & longitude coordinates**
- ✅ **Distance calculations** between zip codes
- ✅ **Demographic Data** by zip code
- ✅ **Income Data** by zip code
- ✅ **Zip Codes in Radius** 

Check the [Zip Code API Documentation](https://metadapi.stoplight.io/docs/api/f4e77dc2eaf4d-zip-code-data-api) for full details of the API. 

To use any of the samples provided in this repository a [Zip Code API](https://www.metadapi.com/API-Products/Zip-Code-API) **key** is needed. 

## Samples

### Python
`samples/Python` folder contanins the following samples:

**Enhance Zip Code Data with Python**:
- Blog article that explains how to [Enhance Zip Code Data with Python](https://www.metadapi.com/Blog/python-code-to-enhance-zip-codes) 
- [`zip-code-append-data-to-file.py`](samples/Python/zip-code-append-data-to-file.py) This example opens a text file with a list of zip codes and then creates a csv files with enhanced data for each of those zip codes using the zip code details API.
- [`sample-zips.txt`](samples/Python/sample-zips.txt) This file contains a list of zip codes. One per line.

**Get Population by Zip Code**:
- Blog article that explains how to [Get Population by Zip Code](https://www.metadapi.com/Blog/get-us-population-by-zip-code)
- [`zip-code-plot-population-growth.py`](samples/Python/zip-code-plot-population-growth.py) This example gets plots the yearly population of multiple zip codes in a line graph. 

**Calling APIs in Parallel**:
- Blog article that explains how to [Call Zip Code APIs in Parallel](https://www.metadapi.com/Blog/maximizing-efficiency-calling-apis-in-parallel)
- [`zip-code-parallel-api-calls.py`](samples/Python/zip-code-parallel-api-calls.py) Python code with example on how to call API's in parallel. 

**Ad targetting zip codes based on income**
- Blog article that explains how to [target specific zip codes based on income thresholds](https://www.metadapi.com/Blog/how-demographic-data-by-zip-code-enhances-ad-targeting)

### Azure Data Factory
`samples/Azure-Data-Factory/Dynamic-API-External-Call` folder contanins the following:

**Dynamically Invoking REST API with Data Factory**:
- Blog article that explains step by step how to [Dynamically Invoking REST API with Data Factory](https://www.metadapi.com/Blog/dynamically-invoking-rest-api-with-data-factory)
- [`metadapi-zip-code-adf-syntax.txt`](samples/Azure-Data-Factory/Dynamic-API-External-Call/metadapi-zip-code-adf-syntax.txt)Azure Data Factory syntax version of the Zip Code API Payload. 
