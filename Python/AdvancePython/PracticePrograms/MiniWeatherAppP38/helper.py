# helper.py

def weather_status(temp):
    if temp > 35:
        return "Hot"
    elif temp > 20:
        return "Pleasant"
    else:
        return "Cold"