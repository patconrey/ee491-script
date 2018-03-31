import datetime
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

samples = []
NUM_SAMPLES = 100000

# Hardware SPI configuration:
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

start = datetime.datetime.now()

for x in range(0, NUM_SAMPLES):
    samples.append(x)

end = datetime.datetime.now()
print("Sample Rate: " + str(NUM_SAMPLES / (end.second - start.second)))
