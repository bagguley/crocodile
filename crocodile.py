import sys
import time
import pifacedigitalio

p = pifacedigitalio.PiFaceDigital()
run = True

def init():
    # Set trigger to 0
    p.output_pins[7].value=0
    
    # Allow module to settle
    time.sleep(0.5)

def ping():
    # Send 10us pulse to trigger
    p.output_pins[7].value=1
    time.sleep(0.00001)
    p.output_pins[7].value=0
    
    # Time the echo
    start=time.time()
    begin=start
    while p.input_pins[0].value==1:
       start=time.time()
       if (start-begin>0.2):
          break
    
    stop=start
    begin=stop
    while p.input_pins[0].value==0:
        stop=time.time()
        if (stop-begin>0.2):
            break
    
    elapsed=stop-start
    
    distance=(34029/2) * elapsed
    
    if (distance < 400):
       print("Distance {:.4f}cm".format(distance))
    
    time.sleep(0.5)

p.gppub.bits[0].value=0
init()
while run==True:
    ping()
    if (p.input_pins[1].value==1):
      run=False
p.deinit_board()
