print("Hello user to calculate the average speed of a body,\ni need some informations and i gonna ask you a few things")

print("\nThat body is moving on km/h or m/s or m/h?: ")

unit_speed = input("\nPrint here: ")

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
