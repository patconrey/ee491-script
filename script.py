# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# Author: Tony DiCola
# License: Public Domain
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
from threading import Timer
from datetime import datetime


Ts = 0.001
WAIT_TIME = 20  # [s]
shouldContinue = True
samples = []

# Hardware SPI configuration:
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# t = Timer(WAIT_TIME, invalidate_timer)
# t.start()

print('Reading MCP3008 values')
# start = datetime.now()

fs = 17601  # Hz
for x in range(0, WAIT_TIME * fs):
    samples.append(mcp.read_adc(0))

file = open('samples.txt', 'w')
for sample in samples:
    file.write("%s\n" % sample)

file.close()
print('Finished writing file, press Ctrl-C to quit...')
# end = datetime.now()
# print("END:     " + str(end))
# print("DIFF:    " + str(end - start))
