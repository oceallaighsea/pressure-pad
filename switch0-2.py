# Firebase Database URL
# https://lccsproject2022-default-rtdb.europe-west1.firebasedatabase.app/
# Get the url as shown above for your database, check the guide.
# Created new database on 15-12... will need to be replaced in 30 days from then

# Purpose of this program is to connect to a microbit via serial link/usb connection
# The microbit will send information depending on which analog pin is pressed.
# A pin is pressed when the circuit is complete. 0 , 1, 2 will be sent from microbit to indicate

# when the data is recieved it will be cleaned and then sent to the database
# A timestamp will also be created and sent to db as this can be used for a lot of things.

import serial
import time
import datetime

from firebase import firebase

myDBConn = firebase.FirebaseApplication('https://lccsproject2022-default-rtdb.europe-west1.firebasedatabase.app/', None)

serCon = serial.Serial()
serCon.baudrate = 115200
serCon.port = "COM18" # This can sometimes change 
serCon.open()
print("SUCCESS WE HAVE GOT THIS FAR ")

while True:
    microbitData = str(serCon.readline())
    print(microbitData)
    switch = microbitData[2:] # slice string from pos 3 to the end of the string
    #Remove spaces from the string
    switch = switch.replace(" ","")
    #Replace the escape characters with an empty char using the replace function()
    switch = switch.replace("\\r\\n","")
    #replace the ' character with ""
    switch = switch.replace("'","")
    #convert the string to an int
    switch = int(switch)
    
    print("switch ",switch, "Was Pressed")
    

    #now = datetime.datetime.now()
    
    now = int(datetime.datetime.today().strftime("%Y%m%d%H%M%S"))# %Y%m%d%H%M%S formats year month day hour min sec
    print(now)
    
    record = {
     "switch" : switch,
     "timeStamp" : now 
    }

    result = myDBConn.post("switch", record)
    #print the unique id that is returned from the firebase database
    print(result)
    
    time.sleep(5)
 
serCon.close()
myDBCon.close()
    
