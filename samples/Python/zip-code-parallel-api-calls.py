#########################################################################################################################
# Name: zip-code-parallel-api-calls.py
# Description: This sample opens a text file with zip codes and for each of the zip codes provided
#             makes a call to the zip code details endpoint in parallel (sending 2 at a time). 
# IMPORTANT: In the code, variable vheaders requires your API Key. Replace the value <YOURZIPKEY> with your API Key
# To get an api key visit: https://metadapi.com
#########################################################################################################################

import requests
import concurrent.futures

# Function to fetch description for a single zipcode
def fetch_description(vzipcode):
    vheaders = {"Ocp-Apim-Subscription-Key": "<YOUR API KEY>"} #CHANGE TO INCLUDE API KEY PROVIDED BY METADAPI.COM
    url = f"https://global.metadapi.com/zipc/v1/zipcodes/{vzipcode}"
    response = requests.get(url, headers=vheaders)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to process codes in parallel
def process_codes_in_parallel(zipcodes):
    descriptions = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_to_code = {executor.submit(fetch_description, zipcode): zipcode for zipcode in zipcodes}
        for future in concurrent.futures.as_completed(future_to_code):
            zipcode = future_to_code[future]
            try:
                description = future.result()
                if description:
                    descriptions.append(description)
            except Exception as e:
                print(f"Failed to fetch description for code {zipcode}: {e}")
    return descriptions

# Read codes from a file
def read_codes_from_file(filename):
    with open(filename, 'r') as file:
        zipcodes = [line.strip() for line in file]
    return zipcodes

# Main function
def main():
    filename = r'sample-zips.txt'  #CHANGE TO INCLUDE PATH AND FILE NAME IN LOCAL ENVIRONMENT
    zipcodes = read_codes_from_file(filename)
    
    # Process codes in chunks
    chunk_size = 2
    for i in range(0, len(zipcodes), chunk_size):
        chunk = zipcodes[i:i+chunk_size]
        descriptions = process_codes_in_parallel(chunk)
        print(descriptions)  # Do whatever you want with the descriptions

if __name__ == "__main__":
    main()
