# Copy and paste your code from the Process Requests activity here!
# This function takes a user request and prints a response based on the user
def copmuter_request(request):
    reponse = str(input("Is your computer plugged in? yes/no"))
    if str(response.lower()) == "yes":
        response = str(input("unplug and replug, did it work? yes/no"))
        if str(response.lower()) == "yes":
            print("great!")
        else:
            print("you may have some other problem.")
    else:
        response = str(input("plug it in, did it work? yes/no"))
        if str(response.lower()) == "yes":
            print("great!")
        else:
            print("you may have some other problem.")


def printer_request(request):
    reponse = str(input("Is your printer plugged in? yes/no"))
    if str(response.lower()) == "yes":
        response = str(input("is there paper in the tray? yes/no"))
        if str(response.lower()) == "yes":
            print("great!")
        else:
            print("put some paper in")
    else:
        response = str(input("plug it in, did it work? yes/no"))
        if str(response.lower()) == "yes":
            print("great!")
        else:
            print("you may have some other problem.")


def internet_request(request):
    reponse = str(input("Is your router plugged in? yes/no"))
    if str(response.lower()) == "yes":
        response = str(input("unplug and replug, did it work? yes/no"))
        if str(response.lower()) == "yes":
            print("great!")
        else:
            print("you may have some other problem.")
    else:
        response = str(input("plug it in, did it work? yes/no"))
        if str(response.lower()) == "yes":
            print("great!")
        else:
            print("you may have some other problem.")


def process_request(request):
    if "internet" in request or "wifi" in request:
        internet_request(request)
        return
    if "print" in request or "scan" in request:
        printer_request(request)
        return
    if "freeze" in request:
        computer_request(request)
        return
    print("no idea watchu talking bout bruh")


# Create a while loop to test process_request
user = ""
print("Welcome to the computer troublshooting chatbot! How can I help you? ")
while not "exit" in user or not "good-bye" in user:
    user = str(input("Issue: "))
    if "exit" in user:
        break
    process_request(user)
    print("Is there anything else I can help with? To leave the chat, type \'exit\' or \'good-bye\'")