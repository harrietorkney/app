from sys import exit

def daytimefood():
    dead("Daytime food output")

def daytimedrink():
    dead("Daytime drink output")

def culturedactivity():
    dead("Cultured activity output")

def niceweather():
    dead("Nice weather output")

def badweather():
    dead("Bad weather output")

def weather():
    print "is the weather ok?"

    choice = raw_input("> ")

    if "yes" in choice:
        niceweather()
    elif "no" in choice:
        badweather()
    else:
        dead("Dunno what ur saying to me!")


def cultured():
    print "are u feelin C.U.L.T.U.R.E.D?"

    choice = raw_input("> ")

    if "yes" in choice:
        culturedactivity()
    elif "no" in choice:
        weather()
    else:
        dead("Dunno what ur saying to me!")


def daytimenotfood():
    print "are u thirsty?"

    choice = raw_input("> ")

    if "yes" in choice:
        daytimedrink()
    elif "no" in choice:
        cultured()
    else:
        dead("Dunno what ur saying to me!")


def day():
    print "ok, so something during the day then.."
    print "are you hungry?"

    choice = raw_input("> ")

    if "yes" in choice:
        daytimefood()
    elif "no" in choice:
        daytimenotfood()
    else:
        dead("Dunno what ur saying to me!")

def nightfood():
    dead("Night food output")

def club():
    dead("club output")

def bar():
    dead("bar output")

def nightdrink():
    print "do u wanna dance as well?"

    choice = raw_input("> ")

    if "yes" in choice:
        club()
    elif "no" in choice:
        bar()
    else:
        dead("Dunno what ur saying to me!")

def nightnotdrink():
    dead("Night not drink output")

def nightnotfood():
    print "are u thirsty?"

    choice = raw_input("> ")

    if "yes" in choice:
        nightdrink()
    elif "no" in choice:
        nightnotdrink()
    else:
        dead("Dunno what ur saying to me!")

def night():
    print "ok, so something in the evening then.."
    print "are you hungry?"

    choice = raw_input("> ")

    if "yes" in choice:
        nightfood()
    elif "no" in choice:
        nightnotfood()
    else:
        dead("Dunno what ur saying to me!")

# this asks what time of day someone wants to go out
def timing():
    print "what time do u wanna go? Day or night?"

    choice = raw_input("> ")
    
    # you need to declare a boolean conditional
    # for both options 
    if "day" in choice:
        day()
    elif "night" in choice:
        night()
    else:
        dead("Dunno what ur saying to me!")


# this is the first question asked
def start():
    print "Hi!! What's ur name?"
    name = raw_input("> ")
    print " %s u wanna do something fun?" % (name)

    choice = raw_input("> ")

    if "ye" in choice:
        timing()
    elif "no" in choice:
        dead("Fine! Stay at home alone then!")
    else:
        dead("Dunno what ur saying to me!")

def dead(why):
    print why
    exit()


start()