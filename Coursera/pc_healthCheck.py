#!/usr/bin/env python3
import shutil
import psutil

# Check if CPU usage is over 75%
def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20


# the cpu is healthy if the usage is less than 75%
def check_cpu_usuage():
    usuage = psutil.cpu_percent(1)
    return usuage < 75

if not check_disk_usage("/") or not check_cpu_usuage():
    print("ERROR!")
else:
    print("Everything is OK!")