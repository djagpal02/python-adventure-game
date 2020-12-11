from random import random
"""
    Used to generate random movement letters to test for errors in moving around the map

    Set shop and bed input to "no" and set battle probabablilty to 0 
"""
def unittester():
    flt = random()
    if flt < 0.25:
        letter = "a"
    elif flt > 0.25 and flt <0.5:
        letter = "s"
    elif flt > 0.5 and flt <0.75:
        letter = "d"
    elif flt > 0.75:
        letter = "w"
    
    return letter