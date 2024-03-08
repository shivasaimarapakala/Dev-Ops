from datetime import *

def elapsedtime(time1,time2):

    # prints the time difference of two given times 
    time_delta = time1 - time2
    days = time_delta.days
    seconds = time_delta.seconds
    if time_delta.days >= 365:
        print(f"{days//365} year(s) ago")
    
    elif time_delta.days >= 30:
        print(f"{days//30} month(s) ago")

    elif time_delta.days >= 7:
        print(f"{days//7} week(s) ago")

    elif time_delta.days >=1:
        print(f"{days} day(s) ago")

    elif time_delta.seconds >= 3600:
        print(f"{seconds//3600} hour(s) ago")
        
    elif time_delta.seconds >= 60:
        print(f"{seconds//60} minute(s) ago")
        
    else:
        print(f"{seconds} seconds(s) ago")
                
    
        

    