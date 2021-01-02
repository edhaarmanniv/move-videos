import datetime as dt
import os

camera_roll_path = os.path.join("mnt","c","Users","Ed","OneDrive","Pictures","Camera Roll")
destination_path_root = os.path.join("/mnt/c/Users/Ed/OneDrive/Documents/Workouts")
# /mnt/c/Users/Ed/OneDrive/Documents/Workouts

with os.scandir(".") as dir_entries:
    for entry in dir_entries:
        info = entry.stat()
        human_readable_time = dt.datetime.fromtimestamp(info.st_ctime)
        print(human_readable_time)