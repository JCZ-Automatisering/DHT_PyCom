import pycom
import time
from dth import DTH

pycom.heartbeat(False)
th = DTH('P10', 1)      # we (JCZ) ues P10
time.sleep(2)
result = th.read()
if result.is_valid():
    print('Temperature: {:3.2f}'.format(result.temperature/1.0))
    print('Humidity: {:3.2f}'.format(result.humidity/1.0))
    pycom.rgbled(0x001000)  # green for 300 ms
    time.sleep(.3)
    pycom.rgbled(0x0)   # off
