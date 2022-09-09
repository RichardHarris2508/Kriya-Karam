# get current temp for NYC, NY from weather.gov (Python 3.4)

import urllib.request

req = urllib.request.Request("http://forecast.weather.gov/MapClick.php?lat=40.7142&lon=-74.0059#.V0T2XI_zzck")
web = urllib.request.urlopen(req)
page = web.readlines()
#these next bits surround the current temperature: 
before_temp = '<p class="myforecast-current-lrg">'
after_temp = "&deg;F</p>"

for line in page:
    current = line.decode("utf-8")
    if before_temp in current and after_temp in current:
        temp = current.replace(before_temp, "")
        temp = temp.replace(after_temp, "")
        temp = temp.strip()
        print("Current temperature: " + temp + " F")
        
web.close()