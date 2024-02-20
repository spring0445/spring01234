import time

def focus_timer(minutes):
    seconds = minutes * 60
    time.sleep(seconds)
    print(f"Focus timer for {minutes} minutes is up! Time to take a break.")

# 设置专注时长为25分钟
focus_timer(25)
