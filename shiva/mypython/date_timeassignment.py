from datetime import *
from elapsedtime import elapsedtime


timelist  = ['2024-03-07 14:20:49.498120','2024-03-07 14:11:02.732620','2024-03-06 22:21:34.332190',
             '2024-03-03 14:29:43.738120','2024-02-22 14:41:34.432120','2023-05-11 14:28:54.932320','2021-09-09 14:21:14.432120']
ref_time = '2024-03-07 14:21:34.432120'

print(f'From the time {ref_time}')

for time2 in timelist :

    print(f"{time2} was {elapsedtime.elapsedtime(ref_time,time2)} ago")





 