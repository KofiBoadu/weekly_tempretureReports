import requests

def location_weather():
    
    try:
        location= input("Enter location: ")
        api_request= requests.get(f"https://weatherdbi.herokuapp.com/data/weather/{location}")
        
        weather_data= api_request.json()
        
        return weather_data
    
    except requests.exceptions.ConnectionError:
        
        print("Could not connect to the server at this time")
    
    
def weather_methods():

    reports= location_weather()

    weather_keys=[]

    for key, value in reports.items():
        
        weather_keys.append(key)

    week_reports= reports[weather_keys[2]]


    return week_reports

        
    
def organizeReports():

    data= weather_methods()

    for items in data:

        for key,value in items.items():

            days= items["day"]
            max_temp=items["max_temp"]["f"]
            min_temp= items["min_temp"]["f"]

        results= print(f"\n{days} \n The highest temp= {max_temp}\n The lowest temp={min_temp}")


    return results
    
    


def tempretureReports():
    
    organizeReports()
        
  
        
      
    
    
tempretureReports()
    
  
    
    