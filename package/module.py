import time


def reverse_time() -> str:
    return f'{time.localtime().tm_sec:02}:{time.localtime().tm_min:02}:{time.localtime().tm_hour:02}'
print(__name__)

