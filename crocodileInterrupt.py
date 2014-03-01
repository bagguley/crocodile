import sys
import errno
import signal
import time
import pifacedigitalio

timeup=[0]
timedown=[0]

def echo_up(event):
   timeup[0]=event.timestamp*1000

def echo_down(event):
   timedown[0]=event.timestamp*1000

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
listener.register(0, pifacedigitalio.IODIR_OFF, echo_up, 0.001)
listener.register(0, pifacedigitalio.IODIR_ON, echo_down, 0.001)

p.output_pins[7].value=0
time.sleep(0.5)

listener.activate()

while exit==False:
   timeup[0]=0.0
   timedown[0]=0.0
   ping()
   print(((34029/2)*(timedown[0]-timeup[0]))/1000)

listener.deactivate()
p.deinit()
