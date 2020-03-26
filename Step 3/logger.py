import microbit as mb
import radio

radio.on()
radio.config(channel=11, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY)

while not mb.button_a.is_pressed():  # wait for button A to be pressed to begin logging
    mb.sleep(10)

radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000) #wait one second
mb.display.show(mb.Image.HEART)  # Display Heart while logging

while not mb.button_a.is_pressed(): # Read and send accelerometer data repeatedly until button A is pressed again
    time = str(mb.running_time()) #time = the running time
    xaccel = str(mb.accelerometer.get_x()) #xacceleration = the x acceleration 
    yaccel = str(mb.accelerometer.get_y())
    zaccel = str(mb.accelerometer.get_z())
    radio.send(time + "," + xaccel + "," + yaccel + "," + zaccel) #send the four values as a tuple separated by commas
    mb.sleep(10) #wait 1/100 of a second before sending new values
    print(xaccel+" "+yaccel+" "+zaccel+" "+ time)
