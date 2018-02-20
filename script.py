# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from threading import Timer


Ts = 1 / 1000
shouldContinue = True
samples = []

# Hardware SPI configuration:
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

def invalidate_timer():
    shouldContinue = False
    print("Suspected Samples: " + str(1/Ts))
    print("Actual Samples: " + str(len(samples)))
    if (1/Ts) == len(samples):
        print("🔥🔥🔥🔥🔥🔥🔥🔥")
    elif float(len(samples)) > 0.9*(1/Ts):
        print("🙁🙁🙁🙁🙁🙁🙁🙁")
    else:
        print("😢😢😢😢😢😢😢😢")


t = Timer(Ts, invalidate_timer)
t.start()

print('Reading MCP3008 values, press Ctrl-C to quit...')
while shouldContinue:
    samples.append(mcp.read_adc(0))
    time.sleep(Ts)
