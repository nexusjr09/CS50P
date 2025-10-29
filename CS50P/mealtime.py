def main():
    result = convert_time()
    if result >= 7 and result <=8:
        print("Breakfast time")
    elif result >=12 and result <=13:
        print("Lunch time") 
    elif result >=18 and result <=19:
        print("dinner time")  
def convert_time():
    time = input("What time is it ?  ")
    hours,minute = time.split(":")
    minute = int(minute)
    minute = minute / 60
    hours = int(hours)
    result = hours + minute
    result = int(result)
    return result
main()