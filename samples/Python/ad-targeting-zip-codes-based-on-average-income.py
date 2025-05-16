#########################################################################################################################
# Name: ad-targeting-zip-codes-based-on-average-income.py
# Description: Code asks for a zip code, radius and income threshold. Returns a table sorted by average income 
#              with the zips that meet the income threshold criteria. 
#              For detailed instructions on this code sample go to https://www.metadapi.com/Blog/how-demographic-data-by-zip-code-enhances-ad-targeting
# IMPORTANT:   In the code, variable vheaders requires your API Key. Replace the value <YOURZIPKEY> with your API Key
#              from metadapi.com
#########################################################################################################################

import requests
import pandas as pd
import time
from tqdm import tqdm

vheaders = {"Ocp-Apim-Subscription-Key": "<YOUR API KEY>"}

def get_zips_in_radius(zipcode, radius):
    # Define the API endpoint
    url = f"https://global.metadapi.com/zipc/v1/radius?radius={radius}&uom=mi&zipcode={zipcode}"
    zips = []

    try:
        # Make the API request
        response = requests.get(url,headers=vheaders)
        response.raise_for_status()  # Raise an error for unsuccessful responses
        
        # Parse the JSON response
        data = response.json()
        for zipresp in data["data"]:
            zips.append(zipresp["zipCode"])
    except requests.exceptions.RequestException as e:
        print('error returning the json')
        print(f"An error occurred: {e}")
        return None

    return zips

# Returns for a zipcode the average agi (adjusted gross income) for the year of 2021
def get_total_returns(zipcode, threshold):
    # Define the API endpoint
    url = f"https://global.metadapi.com/zipc/v1/zipcodes/{zipcode}/soi?year=2021"
    try:
        # Make the API request
        response = requests.get(url,headers=vheaders)
        response.raise_for_status()  # Raise an error for unsuccessful responses
        
        # Parse the JSON response
        data = response.json()
        total_returns = sum(item["returns"] for item in data["data"])
        total_agi = sum(item["adjustedGrossIncome"] for item in data["data"])
        if total_returns > 0 :
                avg_agi = total_agi/total_returns
                meets_threshold = "yes" if avg_agi > threshold else "no"
        else:
            avg_agi = 0
            meets_threshold = "no"
        agi_object = {"zipcode":zipcode, "totalAgi":total_agi, "totalReturns": total_returns, "avgAgi":avg_agi, "threshold" : threshold, "meets_threshold" : meets_threshold}
        time.sleep(0.5)
        return agi_object
    
    except requests.exceptions.RequestException as e:
        print('error returning the json')
        print(f"An error occurred: {e}")
        return None
# --------------------------------    START OF MAIN -----------------------------------------

def main():
    zip_code = input("Enter your ZIP code: ")
    # Validate ZIP code input (optional step, ensuring numeric format)
    while not zip_code.isdigit() or len(zip_code) != 5:
        zip_code = input("Invalid ZIP code. Please enter a valid 5-digit ZIP code: ")

    radius = input("Enter a radius in miles: ")

    # Validate radius input (optional step, ensuring a positive numeric value)
    while not radius.isdigit() or float(radius) <= 0:
        radius = input("Invalid radius. Please enter a positive numeric value: ")
    input_threshold = input("Enter Thresholds in 000's: ")
    # Confirm user inputs
    print(f"You entered ZIP code: {zip_code}")
    print(f"You entered radius: {radius} miles")
    print(f"You entered threshold of: {input_threshold}")
    zipList = get_zips_in_radius(zip_code, radius)
    print(f"The following Zip Codes are within {radius} miles of zip code {zip_code} :")
    print(zipList)
    analysis_dataset = []
    for i in tqdm(range(len(zipList)), desc="Zips Processed"):
        total_returns = get_total_returns(zipList[i], int(input_threshold))
        analysis_dataset.append(total_returns)
    df = pd.DataFrame(analysis_dataset)
    sorted_df = df.sort_values(by="avgAgi", ascending=False)
    print(sorted_df)

if __name__ == "__main__":
    main()
