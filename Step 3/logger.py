import microbit as mb
import radio  # Needs to be imported separately

# Change the channel if other microbits are interfering. (Default=7)
radio.on()  # Turn on radio
radio.config(channel=11, length=100)

print('Program Started')
mb.display.show(mb.Image.HAPPY)

while not mb.button_a.is_pressed():  # wait for button A to be pressed to begin logging
    mb.sleep(10)

radio.send('start') # Send the word 'start' to start the receiver
mb.sleep(1000)
mb.display.show(mb.Image.HEART)  # Display Heart while logging


# Read and send accelerometer data repeatedly until button A is pressed again
while not mb.button_a.is_pressed():
    time = str(mb.running_time())
    xaccel = str(mb.accelerometer.get_x())
    yaccel = str(mb.accelerometer.get_y())
    zaccel = str(mb.accelerometer.get_z())
    radio.send(time + "," + xaccel + "," + yaccel + "," + zaccel)
    mb.sleep(10)
    print(xaccel+" "+yaccel+" "+zaccel+" "+ time)
