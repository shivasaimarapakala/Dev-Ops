from datetime import *
import pytest

def elapsedtime(time1,time2):

    # prints the time difference of two given times 
    time_delta = datetime.strptime(time1,'%Y-%m-%d %H:%M:%S.%f') - datetime.strptime(time2,'%Y-%m-%d %H:%M:%S.%f')
    days = time_delta.days
    seconds = time_delta.seconds
    def nest():
        print("hello")
        
    if time_delta.days >= 365:
        return f"{days//365} year(s)"
    
    elif time_delta.days >= 30:
        return f"{days//30} month(s)"

    elif time_delta.days >= 7:
        return f"{days//7} week(s)"

    elif time_delta.days >=1:
        return f"{days} day(s)"

    elif time_delta.seconds >= 3600:
        return f"{seconds//3600} hour(s)"
        
    elif time_delta.seconds >= 60:
        return f"{seconds//60} minute(s)"
        
    else:
        return f"{seconds} second(s)"
    
    
    
                


timelist  = [('2024-03-07 14:20:49.498120','44 second(s)'),('2024-03-07 14:11:02.732620','10 minute(s)'),('2024-03-06 22:21:34.332190','16 hour(s)'),
             ('2024-03-03 14:29:43.738120','3 day(s)'),('2024-02-22 14:41:34.432120','1 week(s)'),('2023-05-11 14:28:54.932320','10 month(s)')
             ,('2021-09-09 14:21:14.432120','2 year(s)')]
ref_time = '2024-03-07 14:21:34.432120'
    
@pytest.mark.parametrize("time", timelist)

def test_elapsedtime(time):
    
    assert elapsedtime(ref_time,time[0]) == time[1], f"{elapsedtime(ref_time,time[0])} and {time[1]} are not same"  

    
