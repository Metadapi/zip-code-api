#########################################################################################################################
# Name: zip-code-plot-population-growth.py
# Description: Plots a line graph of population growth.
# IMPORTANT: In the code, variable vheaders requires your API Key. Replace the value <YOURZIPKEY> with your API Key
#########################################################################################################################
import requests
import matplotlib.pyplot as plt

def fetch_data_from_api():
    #Replace the string <YOUR API KEY> with a valid metadapi.com API key.
    vheaders = {"Ocp-Apim-Subscription-Key": "<YOUR API KEY>"}
    #Zip code enpoint can receive as parameters a list of zip codes. 
    url = f"https://global.metadapi.com/zipc/v1/zipcodes?zipcode=33009,33967,48201"
    response = requests.get(url,headers=vheaders)    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None
def plot_population_data(data):
    for zipcodes in data['data']:
        years = []
        populations = []
        for zipstats in zipcodes['zipCodeStatistics']:
            years.append(zipstats['year'])
            populations.append(zipstats['totalPopulation'])
        plt.plot(years,populations, label = zipcodes['zipCode'])
    plt.title("Population Over Years")
    plt.xlabel("Year")
    plt.ylabel("Total Population")
    plt.legend()
    plt.show()
    

def main():
    api_data = fetch_data_from_api()

    if api_data:
        plot_population_data(api_data)

if __name__ == "__main__":
    main()



