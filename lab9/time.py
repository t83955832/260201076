import time

def rec_time(n):
    if n==0:
        print("The End.")
        return None
    
    print(f"time remaining:{n}")
    time.sleep(1)
    return rec_time(n-1)


rec_time(3)