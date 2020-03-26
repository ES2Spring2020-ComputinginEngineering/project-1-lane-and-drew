import microbit as mb
import radio 

radio.on() 
radio.config(channel=11, length =100)

print('Program Started')
mb.display.show(mb.Image.HAPPY, delay=1000, clear=True)


# Wait for start message before beginning printing
incoming = ''
while not incoming == 'start':
    incoming = radio.receive()
print('start')

while True:
    incoming = radio.receive() # Read from radio
    if incoming is not None: # message was received
        mb.display.show(mb.Image.HEART, delay=100, clear=True, wait=False) #display heart
        data = tuple(int(info) for info in incoming.split(",")) #data is a tuple of the information received after into is converted to integers 
        print(data) #prints the data to be copied and pasted into a text file
        mb.sleep(10) #wait 1/100 of a second
