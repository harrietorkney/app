from sys import exit

def out_out():
    print "Sweet!"
    print "Ok, I have a couple of Qs for u then"
    print "Do u wanna go out out? Or not?"

    choice = raw_input("> ")

    if "out out" or "sure" or "ye" in choice:
        dead("Ok so a big night then.. Hmm..")
    elif "no" in choice:
        dead("Ok so something in the afternoon or early eve then.. Hmmm..")
    else: 
        dead ("I got no idea what that means.")


def not_out():
    print "ur so boring.."
    print "just say yes! I'll find something rly fun!!!!!"

    choice = raw_input("> ")

    if "yes" in choice:
        out_out()
    elif "no" in choice:
        dead("Fine, suit urself.")
    else:
        dead("u make no sense..")


def dead(why):
    print why, ""
    exit(0)

def start():
    print "m88888888, u wanna do something fun?"

    choice = raw_input("> ")

    if "ye" in choice:
        out_out()
    elif choice == "no":
        not_out()
    else:
        dead("Dunno what ur saying to me!")


start()