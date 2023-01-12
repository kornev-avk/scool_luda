import time
def lost_time(max):
    for x in range(-1, max):
        print(max)
        max -= 1
        time.sleep(1)

lost_time(5)