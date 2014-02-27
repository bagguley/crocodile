import sys
import time
import pifacedigitalio as p

def init():
    # Set trigger to 0
    p.digital_write(7,0)
    
    # Allow module to settle
    time.sleep(0.5)

def ping():
    # Send 10us pulse to trigger
    p.digital_write(7,1)
    time.sleep(0.00001)
    p.digital_write(7,0)
    
    # Time the echo
    #print("Time the echo")
    start=time.time()
    while p.digital_read(0)==1:
       if (time.time()-start)>0.2:
          break
    start=time.time()
    
    #print(pfd.input_pins[0].value)
    #print("Start")
    
    stop=time.time()
    while p.digital_read(0)==0:
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

p.init()
init()
while True:
    ping()
p.deinit()
