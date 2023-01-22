# import requests as requests
# from bs4 import BeautifulSoup
#
# url = 'http://127.0.0.1:5000/text/rsztqwFnxOZevfkQNDd7Muara2hLNL5shyMFMpvbF7wPComgQyBBN02k58F6cbGg2CUbmf6WcB2BM11hgK6guCMaUViTeLqmhFIs6DSK022EDhubFIM5nm4t'
# r = requests.get(url)
# print(r.status_code)
#
# # with open("./sample.jpg", 'wb') as f:
# #     f.write(r.content)
# #from APISystem.models import User, Post, Key, DataKey, RequestsKey
#
#
# #def validate_key(key):  # check: expire_date, data or n requests used.
# #    k = Key.query.filter_by(token=key).first()
# #    if k.expire_date < datetime.datetime.now():
# #        return False
# #    else:
# #        return True
# from datetime import datetime
#
# date_variable = "2023-01-06 09:28:03.063237017"
# date_variable = date_variable[:26]
# timestamp_formatted = datetime.strptime(date_variable, '%Y-%m-%d %H:%M:%S.%f')
# print(timestamp_formatted)

# import datetime
# from datetime import timedelta
#
#
# delta = datetime.timedelta(seconds=5)
# print(delta)
from datetime import datetime
import datetime as dt
packet_number =  2
delta = dt.timedelta(seconds=5)
START = "2023-01-06 09:28:00.011058962"
START = START[:26]
START = datetime.strptime(START, '%Y-%m-%d %H:%M:%S.%f')
END = START + delta*packet_number