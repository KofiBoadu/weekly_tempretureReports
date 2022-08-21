import requests

#Locally installed the request package using pip install request and imported it to make our API request

class TempretureReports:
    def __init__(self,location):
        self.location= location
        self._apiRequests= requests.get(f"https://weatherdbi.herokuapp.com/data/weather/{self.location}")
        self._apiReport= self._apiRequests.json()

#our class has a property that returns a JSON file with weather data that can be further manipulated with 
# further methods if needful

    def weatherData(self):
        reports= self._apiReport
        weatherData=[]
        [weatherData.append(key) for key, value in reports.items()]
        weekData=reports[weatherData[2]]
        return weekData
    # the weatherData method returns only the tempreture data from the API JSON file 


    def weekTempReport(self):
        data= self.weatherData()
        for items in data:
            for _,_ in items.items():
                days= items["day"]
                max_temp=items["max_temp"]["f"]
                min_temp= items["min_temp"]["f"]
            finalReport= print(f"\n{days} \n The highest temp= {max_temp}\n The lowest temp={min_temp}")
        return finalReport

        
#The weekTempReport method manipulates the JSON WEATHER DATA file and returns the formated verison of 
#only the highest and lowest tempreture in FAHAREIT 




    
