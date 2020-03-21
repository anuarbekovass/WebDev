def alarm_clock(day, vacation):
    weekday_alarm = "7:00"
    weekend_alarm = "10:00"
    if vacation:
        weekday_alarm = "10:00"
        weekend_alarm = "off"
    if day>0 and day<6:
        return weekday_alarm
    else:
        return weekend_alarm