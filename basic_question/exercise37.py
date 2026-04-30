import time
def Countdown(n):
    while n > 0:
        time.sleep(1)
        print(n)
        if n == 1:
            print("Blast off! ")
        n -= 1

Timer = int(input("start_count: "))
Countdown(Timer)