
#########################################################################################################################
# Name: zip-code-append-data-to-file.py
# Description: This sample opens a text file with zip codes (in the repository) and for each of the zip codes provided
#             makes a call to the zip code details endpoint, gets specific data elements from the response and 
#             creates a csv file with the enhanced data.
# IMPORTANT: In the code, variable vheaders requires your API Key. Replace the value <YOURZIPKEY> with your API Key
#########################################################################################################################

import requests
import csv

vheaders = {"Ocp-Apim-Subscription-Key": "<YOURZIPKEY>"}

with open(r'sample-zips.txt', 'r') as fp:
    with open('zip-enhanced.csv', 'w',newline='') as f:
        writer = csv.writer(f)
        for line in fp:
            vzipcode = line.strip()
            url = f"https://global.metadapi.com/zipc/v1/zipcodes/{vzipcode}"
            response = requests.get(url,headers=vheaders).json()
            csvline = [vzipcode,response["data"]["stateCode"],response["data"]["stateName"],
                       response["data"]["titleCaseCountyName"],response["data"]["latitude"],response["data"]["longitude"] ]
            writer.writerow(csvline)
            print(csvline)
    