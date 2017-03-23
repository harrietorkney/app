from flask import Flask, render_template, request, session
from sys import exit
from flask_socketio import SocketIO, emit
import webbrowser
import os
import shutil

from googleplaces import GooglePlaces, types, lang
from key import key # You'll need to change this to your own google API key
import pygmaps

  
scenario = ''
session = ''
view = 0


if os.path.exists('./templates/final_map.html'):
	view = 0
	os.remove('./templates/final_map.html')

app = Flask("demo")  

# The line below is there for now ensure session works. Session is a way to store some data between different questions
# the user ask in order to solve the problem of your application not knowing to go to the "night" decision branch
# when the user has answered "night" in one of your question later on! 
#
# You should set the APP_SECRET on your Heroku app setting to ensure it is really kept secret! The 'or "chatbot"'
# part is a shorthand to ensure app.secret_key gets some fallback value ("chatbot") for when you are testing
# this locally on your computer.

app.secret_key = os.getenv('APP_SECRET') or "chatbot"  


socketio = SocketIO(app)
# i = 0

@app.route("/")
def start():
    question1 = "Hi!! What's ur name?"

    
    return render_template("script.html", question1 = question1)

def question1(message):
	return ["%s, u wanna do something fun?" % message]

@socketio.on('connect')
def on_connect():
    print "connected!"


@socketio.on('answer1')
def whats_your_name(message):
	response = question1(message)
	emit ('answer1', response)

@socketio.on('answer2')
def fun(message):
    if message in ["yes", "yeah", "sure", "why not"]:
        response = timing()
        emit('answer2', response)
    elif message in ["no", "nah", "nope", "no thanks"]:
        response = dead()
        emit('answer2', response)
    else:
        response = what()
        emit('answer2', response)

def what():
	# global	i

	# if i < 2:
	# 	i += 1

	return ["Dunno what ur saying to me!"]



	# elif i == 2:
	# 	return dead()


def dead(self):
    socket.emit ["Fine! Stay at home alone then!"]
    exit()
    return()

def timing():

  	return ["What time do you wanna go?", "Day or night?"]

@socketio.on('answer3')
def dayornight(message):
	global session 
	if message in ["day", "am", "daytime", "morning", "afternoon"]:
		session = "day"
		response = dayhungry()
		emit("answer3", response)
	elif message in ["night", "pm", "nighttime", "evening"]:
		session = "night"
		response = nighthungry()
		emit("answer3", response)
	else: 
		response = what()
		emit("answer3", response)
	

def dayhungry():
	return ["ok, so something during the day then..", "feeling peckish?"]

def nighthungry():
	return ["ok, so something in the evening then..", "are you hungry?"]

@socketio.on('answer4')
def is_user_hungry(message):
    # Now reusing the information we have stored earlier in the session to decide which branch of
    # your flow chart to go down.
    global session
    if session == "day":
    	day_hungry(message)
    elif session == "night":
    	night_hungry(message)

@socketio.on('answer4')
def day_hungry(message):
	global session
	if message in ["yes", "yeah", "sure", "why not"]:
		session = "day"
		response = day_food_restaurant()
		emit("answer4", response)
	elif message in ["no", "nah", "nope", "no thanks"]:
		session = "day"
		response = daythirsty()
		emit("answer4", response)
	else:
		response = what()
		emit("answer4", response)

def day_food_restaurant():
	global scenario
	scenario = 'day_food_restaurant'
	return ["Press that red button and I will see what I can find..."]

def daythirsty():
	return ["are u thirsty?"]

@socketio.on('answer4')
def night_hungry(message):
	global session
	if message in ["yes", "yeah", "sure", "why not"]:
		session = "night"
		response = night_food()
		emit('answer4', response)
	elif message in ["no", "nah", "nope", "no thanks"]:
		session = "night"
		response = nightthirsty()
		emit("answer4", response)
	else:
		response = what()
		emit('answer4', response)

def night_food():
	global scenario
	scenario = 'night_food'
	return ['ok let me think', 'Hit the red button!']

def nightthirsty():
	return ["are u thirsty?"]

# @socketio.on('answer5')
# def is_user_thirsty(message):
# 	global session
# 	if session == "day":
# 		day_thirsty(message)
# 	elif session == "night":
# 		night_thirsty(message)

@socketio.on('answer5')
def day_thirsty(message):
	# global session
	if message in ["yes", "yeah", "sure", "why not"]:
		#session = "day"
		response = day_drinks()
		emit("answer5", response)
	elif message in ["no", "nah", "nope", "no thanks"]:
		#session = "day"
		response = cultured_or_not()
		emit("answer5", response)
	else:
		response = what()
		emit("answer5", response)

def day_drinks():
	global scenario
	scenario = 'day_drinks'
	return ["Not a problem", "Try the red button for some ideas"]

def cultured_or_not():
	return["are u feeling C.U.L.T.U.R.E.D?"]


@socketio.on('answer5')
def night_thirsty(message):
	# global session
	if message == "yes":
		#session = "night"
		response = club_or_bar()
		emit ('answer5', response)
	elif message == "no":
		#session = "night"
		response = day_bad_weather_1()
		emit ('answer5', response)
	else:
		response = what()
		emit ('answer5', response)

def day_bad_weather_1():
	global scenario
	scenario = 'day_bad_weather_1'
	return ["OK, ok...", "click the big red button and i'll see what I can find"]

def club_or_bar():
	return ["do u wanna dance as well?"]

# @socketio.on('answer6')
# def user_not_thirsty(message):
# 	# global session
# 	if session == "day":
# 		cultured(message)
# 	elif session == "night":
# 		cluborbar(message)

@socketio.on("answer6")
def cultured(message):
	global session
	if message in ["yes", "yeah", "sure", "why not"]:
		# session = "day"
		response = day_culture()
		emit("answer6", response)
	elif message in ["no", "nah", "nope", "no thanks"]:
		# session = "day"
		response = weather_ok()
		emit = ("answer6", response)
	else:
		response = what()
		emit ("answer6", response)

def weather_ok():
	return ["is the weather OK?"]
def day_culture():
	return ["no problemo... let's have a look see"]

@socketio.on('answer6')
def cluborbar(message):
	# global session
	if message == "yes":
		# session = "night"
		response = night_club()
		emit ('answer6', response)
	elif message =="no":
		# session = "night"
		response = night_bar()
		emit ('answer6', response)
	else:
		response = what()
		emit('answer6', response)

def night_bar():
	global scenario
	scenario = 'night_bar'
	return ["Just some casual drinks then...", "Hit that red button"]

def night_club():
	global scenario
	scenario = 'night_club'
	return ["Good for you you party animal", "Try the red button and I'll show you some options..."]

@socketio.on('answer7')
def day_user_not_thirsty(message):
	# global session
	if session == "day":
		weather_ok(message)


def weather(message):
	if message == "yes":
		response = day_good_weather()
		emit ('answer7', response)
	elif message == "no":
		response = day_bad_weather_1()
		emit ('answer7', response)
	else:
		response = what()
		emit('answer7', response)

def day_good_weather():
	return ["great, let's see now..."]

    
  # print('received json: ' + str(json))
google_places = GooglePlaces(key)

# This is the variable you change depending on outcome
LOCATION = '53.3743452,-1.4980395' # sheffield uni
RADIUS = 2000 # I've just put this as default distance from uni (in metres)

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
mymap = pygmaps.maps(53.3743452,-1.4980395, 14)

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


mymap.draw('./map.html')

count = 0
with open('final_map.html', 'w') as file:
	for line in open('map.html'):
		count += 1
		if count == 3:
			file.write('<link rel="stylesheet" type="text/css" href="map.css"> \n')
		else:
			file.write(line)
file.close()
shutil.move('final_map.html', './templates/final_map.html')

if os.path.exists('./templates/final_map.html'):
	view = 1
else: view =0	

if view == 1:
	@app.route("/map")
	def viewmap():
		return render_template("final_map.html")

if __name__ == '__main__':
    socketio.run(app, debug=True)






