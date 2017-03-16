from googleplaces import GooglePlaces, types, lang
from googleplaces_key import key # You'll need to change this to your own google API key
import pygmaps


# This script uses a google places wrapper code from https://github.com/slimkrazy/python-google-places
# and a module that makes google maps (pygmaps)
# Maybe that's cheating, but it make it way easier.
# you need to install pygmaps and googleplaces for this to work

# This bit reads the API key
google_places = GooglePlaces(key)



# Here is where you specify the scenario based on the outcome from the 'conversation'

# Different scenarios:
# 'day_food_cafe'
# 'day_food_restaurant'
# 'day_drinks'
# 'day_culture'
# 'day_bad_weather_1' - suggests cinema
# 'day_bad_weather_2' - suggets the same as 'day_culture'
# 'day_good_weather'
# 'night_cinema'
# 'night_club'
# 'night_bar'
# 'night_food'

scenario = 'night_food' # This is the variable you change depending on outcome
LOCATION = '53.3743452,-1.4980395' # sheffield uni
RADIUS = 2000 # I've just put this as default distance from uni (in metres)

if scenario == 'day_food_cafe':
    KEYWORD = 'cafe'
    TYPES = [types.TYPE_FOOD]
    rating = 4
elif scenario == 'day_food_restaurant' or 'night_food':
    KEYWORD = 'restaurant'
    TYPES = [types.TYPE_FOOD]
    rating = 4
elif scenario == 'day_drinks':
    KEYWORD = 'pub'
    TYPES = [types.TYPE_BAR]
    rating = 4
elif scenario == 'day_culture' or 'day_bad_weather_2':
    KEYWORD = 'museum'
    TYPES = [types.TYPE_MUSEUM]
    rating = 4
    KEYWORD2 = 'art'
    TYPES2 = [types.TYPE_ART_GALLERY]
elif scenario == 'day_bad_weather_1' or 'night_cinema':
    KEYWORD = 'cinema'
    TYPES = [types.TYPE_MOVIE_THEATER]
    rating = 2
elif scenario == 'day_good_weather':
    KEYWORD = 'park'
    TYPES = [types.TYPE_PARK]
    rating = 3
elif scenario == 'night_club':
    KEYWORD = 'club'
    TYPES = [types.TYPE_NIGHT_CLUB]
    rating = 4
elif scenario == 'night_bar':
    KEYWORD = 'bar'
    TYPES = [types.TYPE_BAR]
    rating = 4

# makes the request and stores the results
query_result = google_places.nearby_search(location=LOCATION, keyword=KEYWORD, radius=RADIUS, types=TYPES)

if query_result.has_attributions:
    print query_result.html_attributions

# create a blank map centred around uni
# the last argument is how much the map is zoomed in (scale of 1-20)
mymap = pygmaps.pygmaps(53.3743452,-1.4980395, 14)

# loop through query result and get info, then plot points on the map
for place in query_result.places:
    place.get_details()
    if place.rating > rating:
        print place.name
        print place.place_id
        mymap.addpoint(place.geo_location['lat'], place.geo_location['lng'], "#0000FF", place.name)

# This bit puts museums and galleries on the same map if the day_culture scenario is chosen
if scenario == 'day_culture' or scenario == 'day_bad_weather_2':
    query_result2 = google_places.nearby_search(location=LOCATION, keyword=KEYWORD2, radius=RADIUS, types=TYPES2)
    if query_result2.has_attributions:
        print query_result2.html_attributions
    for place2 in query_result2.places:
        place2.get_details()
        if place2.rating > rating:
            print place2.name
            print place2.place_id
            mymap.addpoint(place2.geo_location['lat'], place2.geo_location['lng'], "#0000FF", place2.name)

# This produces an html file with points on of all the results.
# If you hover your mouse over the point, it shows the name of the place.
# I haven't figured out how to have the interactive marker where you click on
# it and it tells you more about the place. Hope this is OK.

# The file ends up in whatever folder this script is saved in -- need to figure out
# how to make this map appear in a browser tab. Ask demonstraters this.
mymap.draw('./mymap.html')
