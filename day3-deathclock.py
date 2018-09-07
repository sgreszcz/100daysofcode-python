#!python3

from datetime import datetime
from datetime import timedelta
from datetime import date
import platform
import os
import time

reaper = """\
      %%% %%%%%%%            |#|
    %%%% %%%%%%%%%%%        |#|####
  %%%%% %         %%%       |#|=#####
 %%%%% %   @    @   %%      | | ==####
%%%%%% % (_  ()  )  %%     | |    ===##
%%  %%% %  \_    | %%      | |       =##
%    %%%% %  u^uuu %%     | |         ==#
      %%%% %%%%%%%%%      | |           V
"""

#Stolen from https://stackoverflow.com/questions/15741618/add-one-year-in-current-date-python to handle leapyear/Feb29 date
# To handle leap year (if today is February 29).

def add_years(d, years):
    """Return a date that's `years` years after the date (or datetime)
    object `d`. Return the same calendar date (month and day) in the
    destination year, if it exists, otherwise use the following day
    (thus changing February 29 to March 1).

    """
    try:
        return d.replace(year = d.year + years)
    except ValueError:
        return d + (date(d.year + years, 1, 1) - date(d.year, 1, 1))

name = input ("Please enter your name: ")
print ("\nHello " + name + ". This application will let you know how much time you have left to live.")
print ("\nPlease go to a death date estimator on the web such as:")
print ("www.deathclock.com")
print ("www.death-clock.org")
print ("Or my favorurite:")
print ("https://www.sunlife.co.uk/life-cover/over-50-life-insurance/death-clock/")
print ("Find out how many years you have left to live...\n")

while True:
    try:
        years_left = int(input ("Please enter how many years you have to live: "))
    except ValueError:
        print ("You must enter a valid integer number!")
        continue
    else:
        break

print (years_left)

# datetime objects
now_datetime = datetime.today()
death_datetime = add_years(now_datetime, years_left)

# timedelta object
time_left_in_days = death_datetime - now_datetime

# convert timedelta object into seconds for timer
seconds_left = time_left_in_days.total_seconds()

while seconds_left > 0:
    if platform.system() == "Darwin" or platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == 'Windows':
        os.system('cls')

    print ("You're not dead yet " + name + ".\n")
    # convert seconds left to timedelta object
    time_left = str(timedelta(seconds=round(seconds_left)))
    print ("You have " + time_left + " left!.\n")
    print ("Make the most of it...\n")
    print (reaper)
    time.sleep(1)
    seconds_left -=1






