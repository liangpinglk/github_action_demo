import os
import psutil


def print_memory_info(name):
    """
    印当前程序占用的内存大小
    """
    pid = os.getpid()
    p = psutil.Process(pid)
    a # pylint: disable=C,R,W,E,F

    info = p.memory_full_info()
    mb = 1024 * 1024
    memory = info.uss / mb
    print(f'{name} used {memory} MB')
