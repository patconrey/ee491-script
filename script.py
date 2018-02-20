# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from threading import Timer


Ts = 0.001
WAIT_TIME = 1  # [s]
shouldContinue = True
samples = []

# Hardware SPI configuration:
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

def invalidate_timer():
    shouldContinue = False
    actual = len(samples)
    expected = WAIT_TIME / Ts
    print("Suspected Samples: " + repr(expected))
    print("Actual Samples: " + repr(actual))
    if expected == actual:
        print("Perfect Performance | Sampling: " + repr(actual) + " Out of: " + repr(expected))
    elif actual > 0.9 * expected:
        print("Alright Performance | Sampling: " + repr(actual) + " Out of: " + repr(expected))
    else:
        print("Very Poor Performance | Sampling: " + repr(actual) + " Out of: " + repr(expected))


t = Timer(WAIT_TIME, invalidate_timer)
t.start()

print('Reading MCP3008 values, press Ctrl-C to quit...')
while shouldContinue:
    samples.append(mcp.read_adc(0))
    # time.sleep(Ts)
