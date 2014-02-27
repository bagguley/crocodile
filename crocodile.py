import time
import pifacedigitalio

pfd = pifacedigitalio.PiFaceDigital()

# Set trigger to 0
pfd.output_pins[7].value=0

# Allow module to settle
time.sleep(0.5)

# Send 10us pulse to trigger
pfd.output_pins[7].value=1
time.sleep(0.00001)
pfd.output_pins[7].value=0

# Time the echo
print("Time the echo")
start=time.time()
while pfd.input_pins[0].value==0:
   if (time.time()-start)>1:
      print("break")
      break
start=time.time()

print(pfd.input_pins[0].value)
print("Start")

stop=time.time()
while pfd.input_pins[0].value==1:
   if (time.time()-stop)>1:
      print("break stop")
      break
stop=time.time()

print(pfd.input_pins[0].value)
print("Stop")

elapsed=stop-start

distance=elapsed*34000

distance=distance/2

print("Distance {:.1f}".format(distance))

pfd.deinit_board()
