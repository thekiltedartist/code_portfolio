# You were camping with your friends far away from home, but when it's time to go back, you realize that your fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left.
#
# Considering these factors, write a function that tells you if it is possible to get to the pump or not.
#
# Function should return true if it is possible and false if not.
distance = 50
mpg = 25
gallons_left = 2

def make_it():
    ave_range = gallons_left * mpg
    if ave_range >= distance:
        return True
    else:
        return False


print(f"Will you make it? {make_it()}")
