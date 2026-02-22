print("Hello user to calculate the average speed of a body,\ni need some informations and i gonna ask you a few things")

def km_to_meters(a):

    return a * 1000

def km_to_miles(a):

    return a * 0.621371

def meters_to_km(a):

    return a / 1000

def meters_to_miles(a):

    return a * 0.000621371

def miles_to_km(a):

    return a * 1.60934

def miles_to_meters(a):

    return a * 1609.34

def hours_to_seconds(a):

    return a * 3600

def minutes_to_hours(a):

    return a * 0.0166667

def minutes_to_seconds(a):

    return a * 60

def average_speed(a, b):

    return a / b

distance = (input("what is the distance: "))

type_distance = distance.split()

val_distance = float(type_distance[0])

if "km" in type_distance:

    time = input("How long did it take the body to travel that distance?: ")

    type_time = time.split()

    val_time = float(type_time[0])

    if "hours" in type_time:

        print("The average speed of the body is:\n")

        print(f"{average_speed(val_distance, val_time)}km/h")

        miles = km_to_miles(val_distance)

        print(f"{average_speed(miles, val_time)}m/h")

        meters = km_to_meters(val_distance)

        seconds = hours_to_seconds(val_time)

        print(f"{average_speed(meters, seconds)}m/s")

    elif "minutes" in type_time:

        hours = minutes_to_hours(val_time)

        seconds = minutes_to_seconds(val_time)

        print("The average speed of the body is:\n")

        print(f"{average_speed(val_distance, hours)}km/h")

        miles = km_to_miles(val_distance)

        print(f"{average_speed(miles, hours)}m/h")

        meters = km_to_meters(val_distance)

        print(f"{average_speed(meters, seconds)}m/s")



elif "miles" in type_distance:

    time = input("How long did it take the body to travel that distance?: ")

    type_time = time.split()

    val_time = float(type_time[0])

    if "hours" in type_time:

        meters = miles_to_meters(val_distance)

        km = miles_to_km(val_distance)

        print("The average speed of the body is:\n")

        print(f"{average_speed(km, val_time)}km/h")

        print(f"{average_speed(val_distance, val_time)}m/h")

        seconds = hours_to_seconds(val_time)

        print(f"{average_speed(meters, seconds)}m/s")

    elif "minutes" in type_time:

        hours = minutes_to_hours(val_time)

        seconds = minutes_to_seconds(val_time)

        meters = miles_to_meters(val_distance)

        km = miles_to_km(val_distance)

        print("The average speed of the body is:\n")

        print(f"{average_speed(km, hours)}km/h")

        print(f"{average_speed(val_distance, hours)}m/h")

        print(f"{average_speed(meters, seconds)}m/s")

elif "meters" in type_distance:

    time = input("How long did it take the body to travel that distance?: ")

    type_time = time.split()

    val_time = float(type_time[0])

    if "hours" in type_time:

        miles = meters_to_miles(val_distance)

        km = meters_to_km(val_distance)

        print("The average speed of the body is:\n")

        print(f"{average_speed(km, val_time)}km/h")

        print(f"{average_speed(miles, val_time)}m/h")

        seconds = hours_to_seconds(val_time)

        print(f"{average_speed(val_distance, seconds)}m/s")

    elif "minutes" in type_time:

        miles = meters_to_miles(val_distance)

        km = meters_to_km(val_distance)

        hours = minutes_to_hours(val_time)

        seconds = minutes_to_seconds(val_time)

        print("The average speed of the body is:\n")

        print(f"{average_speed(km, hours)}km/h")

        print(f"{average_speed(miles, hours)}m/h")
        
        print(f"{average_speed(val_distance, seconds)}m/s")