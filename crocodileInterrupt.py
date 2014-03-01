import sys
import pifacedigitalio

p = pifacedigitalio.PiFaceDigital()
listener = pifacedigitalio.InputEventListener(chip=p)
listener.register(0, pifacedigitalio.IODIR_OFF, echo_up, 0.0001)
listener.register(0, pifacedigitalio.IODIR_ON, echo_down, 0.0001)


def echo_up():
   print("up")

def echo_down():
   print("down")

def ping():
    # Send 10us pulse to trigger
    pifacedigitalio.digital_write(7,1)
    time.sleep(0.00001)
    pifacedigitalio.digital_write(7,0)
    time.sleep(0.05)

p.output_pins[7]=0
time.sleep(0.5)

while True:
   ping()
p.deinit()
