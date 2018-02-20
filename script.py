# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from threading import Timer


Ts = 0.0001
shouldContinue = True
samples = []

# Hardware SPI configuration:
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

def invalidate_timer():
    shouldContinue = False
    print("Suspected Samples: " + repr(float(1/Ts)))
    print("Actual Samples: " + repr(len(samples)))
    if (1/Ts) == len(samples):
        print("Perfect Performance | Sampling: " + repr(len(samples)) + " Out of: " + repr(1 / Ts))
    elif float(len(samples)) > 0.9*(1/Ts):
        print("Alright Performance | Sampling: " + repr(len(samples)) + " Out of: " + repr(1 / Ts))
    else:
        print("Very Poor Performance | Sampling: " + repr(len(samples)) + " Out of: " + repr(1/Ts))


t = Timer(Ts, invalidate_timer)
t.start()

print('Reading MCP3008 values, press Ctrl-C to quit...')
while shouldContinue:
    samples.append(mcp.read_adc(0))
    time.sleep(Ts)
