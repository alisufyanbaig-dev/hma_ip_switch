import os
import time

wait_time = 25

for iteration in range(99999999):
    print(iteration)
    time.sleep(wait_time)
    os.system("taskkill /IM openvpn.exe /F")
    print("Killed")