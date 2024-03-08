
def add_time(start, duration, show_day= None):
    week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    colon_pos= start.find(":")
    space_pos= start.find(" ")
    hours = start[:colon_pos]
    minutes = start[colon_pos+1:space_pos]
    day_night = start[space_pos+1:]

    colon_pos1= duration.find(":")
    dur_hours = duration[:colon_pos1]
    dur_minutes = duration[colon_pos1+1:]
    total_duration_in_minutes = (int(dur_hours) * 60) + int(dur_minutes)


    day = []
    part_day = day_night
    hh= int(hours)
    mm = int(minutes)
    for i in range(total_duration_in_minutes):
        
        if mm == 59:
            mm= 0
            if hh == 11:
                hh +=1
                part_day = "PM" if part_day == "AM" else "AM"
                day.append(part_day)
            elif hh == 12:
                hh= 1
            else: hh+=1
        else: mm +=1
    
    if day.count("AM") == 1:
        x= "(next day)"
        
    elif day.count("AM") >= 2:
       days_num =day.count("AM")
       x= f"({days_num} days later)"
    
    else: x=""

    if show_day != None:
        show_day = show_day.capitalize()
        day_index = week.index(show_day)
        current_day = week[day_index + day.count("AM")]
        if week.index(current_day) == week.index(show_day) + 1:
            x = "(next day)"
            current_day = ""
        else: current_day = f", {current_day}"
    else: current_day = ""

    print(f'Returns: {str(hh).rjust(2," ")}:{str(mm).zfill(2)} {part_day}{current_day} {x}')

add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

add_time("11:43 PM", "24:20", "tuesday")
# Returns: 12:03 AM, Thursday (2 days later)

add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)
