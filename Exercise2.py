import time
hour=int(time.strftime("%H"))
Min=int(time.strftime("%M"))
Sec=int(time.strftime("%S"))
if(hour>0 and hour<12):
    print("GOOD MORNING")
elif(hour>12 and hour<16):
    print("GOOD AFTERNOON")
elif(hour>16 and hour<=24):
    print("GOOD NIGHT")
else:
    print("TIME ERROR")
