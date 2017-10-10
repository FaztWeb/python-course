def minutes_to_hours(minutes):
    hours = minutes / 60
    return hours

def seconds_to_hours(seconds):
    hours = seconds / 3600;
    return hours

# two arguments
# default arguments and non-default arguments
def minutes_to_hours2(minutes = 60 , seconds = 0):
    hours = minutes / 60 + seconds / 3600
    return hours

print(str(minutes_to_hours(70)) + " minutes")
print(str(seconds_to_hours(7200)) + " hours")
print(str(minutes_to_hours2()) + " hours")
