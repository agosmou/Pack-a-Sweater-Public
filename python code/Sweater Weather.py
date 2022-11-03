
#import os
import keys # run the keys script by importing
import meteorological_data # run the meterological data
import sys
from twilio.rest import Client
import requests
import json




# Find your Account SID and Auth Token in Account Info and set the environment variables.
# See http://twil.io/secure

class weather:
    # Initialize the object
    def __init__(self, location, lowTemp):
        self.__location = location
        self.__lowTemp = lowTemp

    # mutator for attributes
    def set_location(self, location):
        self.__location = location

    def set_lowTemp(self, lowTemp):
        self.__lowTemp = lowTemp

    # accessor for attributes
    def get_location(self):
        return self.__location
    
    def get_lowTemp(self):
        return self.__lowTemp
    

class location1 (weather):
    # initializing the object with attributes from super class
    def __init__(self, location, lowTemp):

        # Call the superclass __init__ method
        weather.__init__(self, location, lowTemp)
        
def main():

    #User inputted location
    location = 'Los Angeles'

    
    
    # Hard enter this value if you want to test a user inputted, "sweaterTemp"
    #sweaterTemp = 80

    #########################
    # Today's weather temp in F at 5pm PST, pulling from meteorological_data.py
    lowestTempF = meteorological_data.eveningLowTemp #This will print out an integer in celsius
    sweaterTemp = lowestTempF

    #########################

    #convert integer to string for lowest temp
    lowTemp = str(sweaterTemp)
        

    # User input for my lowest temperature I can go without wearing a sweater
    sweaterActivatorTemp = 70

    # create an instance
    my_location = location1(location, lowTemp)


    # use if statement for comparing the integer value of lowest temp withstood to lowTemp
    if sweaterTemp <= sweaterActivatorTemp:
        textMessage = "For this city, " + my_location.get_location() 
        textMessage = textMessage + ", the weather will drop today to " + my_location.get_lowTemp() + "F."
        textMessage = textMessage + " It's sweater weather."

    else:
        sys.exit("Enjoy the weather! - Leave your sweater at home")
    
    
    # Pulling from keys.py to get the API keys
    client = Client(keys.account_sid, keys.auth_token)

    # message to be sent to my cell
    message = client.messages.create(
    body = textMessage,
    from_=keys.twilio_number,
    to=keys.my_number
    )

    # printing it as a pseudo-receipt to see what was sent to my cell
    print(message.body)

# Execute the main function
if __name__ == '__main__':
    main()
