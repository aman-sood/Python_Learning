import ntplib
from time import ctime
from datetime import datetime

# Will print system time. If system time is wrong this fails
print('System time :', datetime.now())

# Will use NTP to get accurate Atomic time on network
# Library refernce https://pypi.python.org/pypi/ntplib/0.3.2
# need to install ntplib
c = ntplib.NTPClient()
response = c.request('europe.pool.ntp.org', version = 3)
print('Atomic time :', ctime(response.tx_time))

