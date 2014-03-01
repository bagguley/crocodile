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

exit = False
p = pifacedigitalio.PiFaceDigital()
uplistener = pifacedigitalio.InputEventListener(chip=p)
downlistener = pifacedigitalio.InputEventListener(chip=p)
uplistener.register(0, pifacedigitalio.IODIR_OFF, echo_up, 0.0001)
downlistener.register(0, pifacedigitalio.IODIR_ON, echo_down, 0.0001)

p.output_pins[7].value=0
time.sleep(0.5)

uplistener.activate()
downlistener.activate()

while exit==False:
   timeup[0]=0.0
   timedown[0]=0.0
   ping()
   print(((34029/2)*(timedown[0]-timeup[0]))/1000)
   if (p.input_pins[1].value==1:
      exit=True

uplistener.deactivate()
downlistener.deactivate()
p.deinit_board()
