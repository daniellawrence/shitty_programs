#!/usr/bin/env python
import io

ERR_PERMISSION = 13


def find_root_disk():
    with open('/proc/mounts') as f:
        mounts = f.readlines()

    for mount_line in mounts:
        disk, mount_point = mount_line.split()[0:2]
        if mount_point == '/':
            return disk

def read_file_into_dev_null(path):
    try:
        with io.open(path) as root_device:
            with open('/dev/null') as devnull:
                devnull.write(root_device.read())
    except IOError as error:
        print("This shitty program failed... with the following error")
        print("    {0}".format(error))
        if error.errno ==  ERR_PERMISSION:
            print("You could try running this as the root user.")


if __name__ == '__main__':
    root_disk = find_root_disk()
    read_file_into_dev_null(root_disk)
