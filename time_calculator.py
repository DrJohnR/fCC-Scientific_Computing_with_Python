# ---test---
day = 'wedNESday'
# day = None
start = '5:01 AM'
duration = '42:59'

# ---routine---
daysList = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
meriList = ['AM', 'PM']

time_, meri = start.split()
hours, mins = time_.split(':')
durHours, durMins = duration.split(':')

sumHours, sumMins = int(hours) + int(durHours), int(mins) + int(durMins)
addHours = int(durHours) + sumMins//60
totHours = int(hours) + addHours
modMins = sumMins%60
meriIndex = meriList.index(meri)

# minutes
if modMins < 10:
    endMins = '0' + str(modMins)
else: endMins = modMins
# hours
endHours = totHours%12
if endHours == 0:
    endHours = 12
# meridiem
if (int(hours) < 12 and totHours%24 < 12) or (int(hours) == 12 and totHours%24 >= 12):
    endMeri = meri
else:
    endMeri = meriList[(meriIndex + 1)%2]
# daysLater
daysLater = addHours//24 - (int(hours)//12) * (1 + meriIndex)%2
if totHours - daysLater*24 >= 24 - 12*meriIndex * (1 + int(hours)//12)%2:
    daysLater +=1

if daysLater == 0:
    daysLaterString = ''
elif daysLater == 1:
    daysLaterString = '(next day)'
else:
    daysLaterString = f'({daysLater} days later)'

# newDay
if day != None:
    dayIndex = daysList.index( day.lower().capitalize() )
    newDay = daysList[(dayIndex + daysLater)%7]
else:
     dayIndex = None

# output
if day != None and daysLater !=0:
    print(str(endHours)+':'+str(endMins),endMeri+',', newDay, daysLaterString)
elif day != None:
    print(str(endHours)+':'+str(endMins),endMeri+',', newDay)
else:
    print(str(endHours)+':'+str(endMins), endMeri, daysLaterString)



# alternative daysLater (1):
# if int(hours) == 12:
#     daysLater = addHours//24 - (meriIndex + 1)%2
#     extraHours = addHours - daysLater*24
#     if int(hours) + extraHours >= 24:
#         daysLater +=1
# else:
#     daysLater = addHours//24
#     extraHours = addHours - daysLater*24
#     if int(hours) + extraHours >= 24 - 12*meriIndex:
#         daysLater +=1

# alternative daysLater (2):
# daysLater = addHours//24 - (int(hours)//12)*(meriIndex + 1)%2
# extraHours = addHours - daysLater*24
# if int(hours) + extraHours >= 24 - (1 + int(hours)//12)%2 * 12*meriIndex:
#     daysLater +=1

# alternative daysLater (3):
# daysLater = addHours//24 - (int(hours)//12)*(meriIndex + 1)%2
# if int(hours) + addHours - daysLater*24 >= 24 - (1 + int(hours)//12)%2 * 12*meriIndex:
#     daysLater +=1
