import time
import win32file


def detect_usb_insertion():
    print('Waiting for pendrive insertion...')

    existing_drives = []
    drives = win32file.GetLogicalDrives()

    for drive in range(1, drives):
        mask = 1 << drive
        if drives & mask:
            drive_name = '{}:\\'.format(chr(drive + 65))
            existing_drives.append(drive_name)

    while True:
        drives = win32file.GetLogicalDrives()
        for drive in range(1, drives):
            mask = 1 << drive
            if drives & mask:
                drive_name = '{}:\\'.format(chr(drive + 65))
                if drive_name not in existing_drives:
                    print('Inserted pendrive:', drive_name)
                    return drive_name
        time.sleep(0.25)


detect_usb_insertion()
