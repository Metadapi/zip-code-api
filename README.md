# zip-code-api
---
## Overview

The Zip Code API provides United States zip code data with a comprehensive data model in JSON format. Using REST design, this API can help you build zip validations, city searches, distance calculations, radius searches and many other key functions for your applications.

This repository contains sample code that can help demonstrate some of the functionality the **Zip Code API** enables. 

To use any of the samples provided in this repository a [Zip Code API](https://www.metadapi.com/API-Products/Zip-Code-API) key is needed. 

## Samples

### Python
`samples/Python` folder contanins the following:

- `zip-code-append-data-to-file.py` This example opens a text file with a list of zip codes and then creates a csv files with enhanced data for each of those zip codes using the zip code details API.
- `sample-zips.txt` This file contains a list of zip codes. One per line.

`samples/Azure-Data-Factory/Dynamic-API-External-Call` folder contanins the following:

- `metadapi-zip-code-adf-syntax,txt` Azure Data Factory syntax version of the Zip Code API Payload. 