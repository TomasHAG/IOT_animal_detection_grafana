import detector
import time
import light_manager
import lora_callbacks

def send(port): # send wether data from memory to a specifik port
    s.bind(port) # bind to the new port
    s.send(0xFF) # send a trigger payload

def loop(): # internal loop to detect and send data
    counter = 0
    while True:
        time.sleep(2) # loop in 2 sec intervalls
        counter += 1
        if detector.read():
            send(2) # send in port 2 that an animal have ben detected
            time.sleep(1*60) # after detection trigger sleep for 1 minute
            counter = 0 # reset echo counter
        elif counter > 10*30: # every 10 minutes
            send(3) #port 3 is for echo calls
            counter = 0 # reset echo counter

loop()
