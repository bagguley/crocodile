import sys
import errno
import signal
import time
import pifacedigitalio

def echo_up(event):
   print("up")

def echo_down(event):
   print("down")

def ping():
    # Send 10us pulse to trigger
    p.output_pins[7].value=1
    time.sleep(0.00001)
    p.output_pins[7].value=0
    time.sleep(0.05)

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
   ping()

listener.deactivate()
p.deinit()
