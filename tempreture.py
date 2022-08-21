import requests

class TempretureReports:
    def __init__(self,location):
        self.location= location
        self._apiRequests= requests.get(f"https://weatherdbi.herokuapp.com/data/weather/{self.location}")
        self._apiReport= self._apiRequests.json()


    def weatherData(self):
        reports= self._apiReport
        weatherData=[]
        [weatherData.append(key) for key, value in reports.items()]
        weekData=reports[weatherData[2]]
        return weekData


    def weekTempReport(self):
        data= self.weatherData()
        for items in data:
            for _,_ in items.items():
                days= items["day"]
                max_temp=items["max_temp"]["f"]
                min_temp= items["min_temp"]["f"]
            finalReport= print(f"\n{days} \n The highest temp= {max_temp}\n The lowest temp={min_temp}")
        return finalReport





    
