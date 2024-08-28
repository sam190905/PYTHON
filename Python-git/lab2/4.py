import datetime
import pytz

ist=pytz.timezone('Asia/Kolkata')
now = datetime.datetime.now(ist)
print(now.strftime("%a %B %d %H:%M:%S %Z %Y"))