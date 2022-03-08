
def add_time(start, duration, day=None):
    week = {1:"monday", 2:"tuesday", 3:"wednesday", 4:"thursday", 5:"friday", 6:"saturday", 7:"sunday"}
    #split the PM, hour, and minutes
    time_period = start.split(" ")
    hour_minute = time_period[0].split(":")
    hour_minute_duration = duration.split(":")

    #time starts at 12 not 0 i.e 0:00 AM == 12:00AM
    if time_period[1] == "PM" and int(hour_minute[0]) != 12:
        hour = int(hour_minute[0]) + 12
    elif time_period[1] == "AM" and int(hour_minute[0]) == 12:
        hour = 0
    else:
        hour = int(hour_minute[0])
    #get the remaining minutes and additional hours if the minutes pass 60
    add_hour = (int(hour_minute[1]) + int(hour_minute_duration[1])) // 60
    remain_minute = (int(hour_minute[1]) + int(hour_minute_duration[1])) % 60
    remain_minute = str(remain_minute)
    #appends 0 on the front when minute is single digit
    if len(remain_minute) == 1:
        remain_minute = "0" + remain_minute
    total_hour = hour + int(hour_minute_duration[0]) + add_hour
    #get the days added when the total hour surpasses 23
    add_days = 0
    if total_hour >= 24 :
        add_days = total_hour // 24
        total_hour = total_hour % 24
    
    if total_hour > 12 :
        period = "PM"
        total_hour = total_hour % 12
    elif total_hour == 12 :
        period = "PM"
    elif total_hour == 0:
        period = "AM"
        total_hour = 12
    else:
        period = "AM"
    
    #this part is to determine what day of the week it is
    if day == None:
        new_time = str(total_hour) + ":" + remain_minute + " " + period
    else:
        day_num = list(week.keys())[list(week.values()).index(day.lower())]
        if day_num + add_days > 7:
            new_day = (day_num + add_days) % 7
        else:
            new_day = day_num + add_days
        new_time = str(total_hour) + ":" + remain_minute + " " + period + ", " + week[new_day][0].upper()+week[new_day][1:]

    # this part is for the 'days later' part
    if add_days == 1 :
        new_time += " (next day)"
    elif add_days > 1 :
        new_time += " (" + str(add_days) + " days later)"
    return new_time

        #current Time, Time added, day of the week
print(add_time("8:16 PM", "466:02", "tuesday"))