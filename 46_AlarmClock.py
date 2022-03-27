# Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a
# boolean indicating vacation, return a string of the form "7:00" indicating
# when the alarm clock should ring. Weekdays, the alarm should be "7:00"
# and on the weekend it should be "10:00".
# On vacation weekdays it should be "10:00" and weekends it should be "off".

def alarm_clock(day, vacation):
    weekday = [1, 2, 3, 4, 5]
    weekend = [6, 0]
    if day in weekday and vacation == False:
        return '7:00'
    elif day in weekend and vacation == False:
        return '10:00'
    elif day in weekday and vacation == True:
        return '10:00'
    elif day in weekend and vacation == True:
        return 'off'

print(alarm_clock(1, False))
print(alarm_clock(5, False))
print(alarm_clock(0, False))
