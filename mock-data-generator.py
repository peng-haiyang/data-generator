import pandas as pd
import numpy as np
import datetime as dt
import random
from random import randrange
import os
import hashlib

users_profile = {
    "UserID":"", # registered user use fixed ID, otherwise assign random hash ID
    "City":"",
    "Gender":"",
    "Age":"",
    "RegisterDate":"",
}

voiijer_page = {
    "VoiijerID":"", # registered user use fixed ID, otherwise assign random hash ID
    "PageID":"",
    "Url":"",
}

session_info = {
    "SessionID":"",
    "UserID":"", # Registered user use fixed ID, otherwise assign random hash ID
    "Sources":"", # Organic or paid ads or last page in VOIIJ
    "SessionStartTime":"", # Timestamp when a session starts
    "SessionEndTime":"", # By GA
    "PageID":"",
    "RegisterButtonHitTimestamp":"",
    "ReviewCheckTimestamp":"",
    "ShareTimestamp":"",
    "ReserveTimestamp":"",
    "PaymentTimestamp":"",
    "PaymentType":"",
    "PaymentStartTimestamp":"",
    "PaymentFinishTimestamp":"",
    "PaymentAmount":"",
}

# a complete journey: home page, voiijiers list page,a voiijer page (dynamic), 
# registration page, the voiijer page (dynamic), reservation, payment
common_page = {
    "01":"HomePage",
    "02":"VooijListPage",
    "03":"RegisPage",
    "04":"ReserPage",
    "05":"PayPage"}

cities = ["Salty Lake City", 
          "West Valley City",
          "Provo",
          "West Jordan",
          "Orem"]
genders = ["M", "F"]
ages = list(range(20,40))
sources = ["Google", "Bing", "Facebook", "Twitter", "Organic"]
PageID = ["VOIIJerPageID{:02d}".format(i) for i in range(10)]

def random_date(start=dt.datetime(2015, 7, 1, 0, 0, 0)):
    current = start
    curr = current + dt.timedelta(days=randrange(30), hours=randrange(24), minutes=randrange(60), seconds=randrange(60))
    return curr
# example
#start_date = dt.datetime(2015, 7, 1, 0, 0, 0)
#for x in random_date(start_date, 3):
#    print(x)
#2016-06-15 09:38:43
#2016-08-03 05:23:12
#2016-04-10 19:50:39
# 20150701 20161231

user_db_array = np.empty((0,5))
for i in range(50):
    result = [hashlib.md5(os.urandom(8)).hexdigest(),
              random.choice(cities),
              random.choice(genders),
              random.choice(ages),
              random_date()]
    user_db_array = np.append(user_db_array, [result], axis=0)


# Create user database
user_db = pd.DataFrame(user_db_array,columns=[i for i in users_profile])

user_db.to_csv("user_database.csv",index=False)


# Generate traffic using registered users information
session_array_reg = np.empty((0,6))
for i in range(5000):
    
    # Get a random start time
    rand_start_time = dt.datetime(2015, 8, 1, 0, 0, 0)
    start_time = random_date(rand_start_time)
    # Get a random end time
    end_time = start_time + dt.timedelta(minutes=randrange(5), seconds=randrange(60))
    
    result = [random.getrandbits(64), # session ID
              random.choice(user_db.UserID), # for registered user
              random.choice(sources), # from which source
              start_time, # SessionStartTime
              end_time, # SessionEndTime
              random.choice(PageID)]
    
    session_array_reg = np.append(session_array_reg, [result], axis=0)

# Create simple traffic dataset
session_db = pd.DataFrame(session_array_reg,columns=[i for i in list(session_info)[0:6]])

session_db.to_csv("session_database.csv", index=False)