# pip install phonenumbers
# pip install folium
# pip install opencage


# track location with the map using the phone number
import phonenumbers
'''
We will import geocoder and carrier modules to get the geological 
location and the service provider name, respectively.
'''
from phonenumbers import geocoder
from phonenumbers import carrier

import folium

from opencage.geocoder import OpenCageGeocode

# taking input the phonenumber along with the country code
number = input("Enter the PhoneNumber with the country code : ")
'''
Now that we have taken the input of the phone number in the form of a string, 
we need to convert it into phone number format, 
and this is done using the parse( ) method of phonenumber module.
'''

# Parsing the phonenumber string to convert it into phonenumber format
phoneNumber = phonenumbers.parse(number)

'''
We will store the API Key that we saved in the Notepad into the Key variable.
'''
# Storing the API Key in the Key variable
Key = "5c835ea02a7f49ca86b8d55483f64947+63 951 177 8365"

'''
We will be using the phoneNumber to print the geo-location 
and service provider name of the entered phone number.
'''
# Using the geocoder module of phonenumbers to print the Location in console
yourLocation = geocoder.description_for_number(phoneNumber, "en")
print(("location : " + yourLocation))

'''
We print the carrier/service provider name with the help of 
the name_for_number( ) method from the carrier module.
'''

# Using the carrier module of phonenumbers to print the service provider name in console
yourServiceProvider = carrier.name_for_number(phoneNumber, "en")
print(("service provider : " + yourServiceProvider))

'''
We extract the complete location using the API key with the opencage methods
'''
# Using opencage to get the latitude and longitude of the location
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)

'''
Now, we use results to get the latitude and longitude of the location we are tracking
'''
# Assigning the latitude and longitude values to the lat and lng variables
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

'''
After, we use Map() method from folium to get the map of given latitude and longitude
'''
# Getting the map for the given latitude and longitude
myMap = folium.Map(loction=[lat, lng], zoom_start=9)
'''
We also use the Marker() method from folium to mark the location with the location name on the map.
'''
# Adding a Marker on the map to show the location name
folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

# save map to html file to open it and see the actual location in map format
myMap.save("Location.html")