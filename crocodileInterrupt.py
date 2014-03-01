import sys
import errno
import signal
import time
import pifacedigitalio

timeup=0.0
timedown=0.0

def echo_up(event):
   timeup=event.timestamp
   print(timeup)

def echo_down(event):
   timedown=event.timestamp
   print(timedown)

def ping():
    # Send 10us pulse to trigger
    p.output_pins[7].value=1
    time.sleep(0.00001)
    p.output_pins[7].value=0
    time.sleep(0.5)

def handler(signum, frame):
    exit=True

signal.signal(signal.SIGINT, handler)

exit = False
p = pifacedigitalio.PiFaceDigital()
listener = pifacedigitalio.InputEventListener(chip=p)
listener.register(0, pifacedigitalio.IODIR_OFF, echo_up, 0.0001)
listener.register(0, pifacedigitalio.IODIR_ON, echo_down, 0.0001)

p.output_pins[7].value=0
time.sleep(0.5)

listener.activate()

while exit==False:
   timeup=0.0
   timedown=0.0
   ping()
   print(timedown-timeup)

listener.deactivate()
p.deinit()
