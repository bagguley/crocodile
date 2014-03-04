import sys
import time
import pifacedigitalio

p = pifacedigitalio.PiFaceDigital()
run = True

def init():
    # Set trigger to 0
    p.output_pins[7].value=0
    p.output_pins[6].value=1
    p.output_pins[5].value=1
    
    # Allow module to settle
    time.sleep(0.5)

def snap():
    print("SNAP!")
    p.output_pins[6].value=0
    time.sleep(0.5)
    p.output_pins[6].value=1
    time.sleep(0.5)
    p.output_pins[5].value=0
    time.sleep(0.5)
    p.output_pins[5].value=1
    time.sleep(2.0)

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
          return -1
    
    stop=start
    begin=stop
    while p.input_pins[0].value==0:
        stop=time.time()
        if (stop-begin>0.2):
            return -2
    
    elapsed=stop-start
    
    distance=(34029/2) * elapsed
    
    time.sleep(0.3)
    return distance

p.gppub.bits[0].value=0
p.output_pins[6].value=1
init()
previousT = 100
count = 0
while run==True:
    t = ping()
    if (t == 0):
       count +=1
    else:
       count = 0

    if (count > 3):
       snap()

    print("Distance {:.4f}cm".format(t))
    if (p.input_pins[1].value==1):
      run=False
p.deinit_board()
