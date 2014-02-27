import sys
import time
import pifacedigitalio

pfd = pifacedigitalio.PiFaceDigital()

def init():
    # Set trigger to 0
    pfd.output_pins[7].value=0
    
    # Allow module to settle
    time.sleep(0.5)

def ping():
    # Send 10us pulse to trigger
    pfd.output_pins[7].value=1
    time.sleep(0.00001)
    pfd.output_pins[7].value=0
    
    # Time the echo
    #print("Time the echo")
    start=time.time()
    while pfd.input_pins[0].value==1:
       if (time.time()-start)>0.2:
          break
    start=time.time()
    
    #print(pfd.input_pins[0].value)
    #print("Start")
    
    stop=time.time()
    while pfd.input_pins[0].value==0:
        if (time.time()-stop)>0.2:
            break
    stop=time.time()
    
    #print(pfd.input_pins[0].value)
    #print("Stop")
    
    elapsed=stop-start
    
    distance=(34290/2) * elapsed
    
    if (distance < 400):
        print("Distance {:.1f}".format(distance))
    
    time.sleep(0.05)

init()
while True:
    ping()
pfd.deinit_board()
