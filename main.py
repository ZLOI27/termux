from time import *
from package.module import reverse_time


def main() -> None:
    hms = localtime()
    print(f'time -> {hms.tm_hour:02}:{hms.tm_min:02}:{hms.tm_sec:02}')
    print(f'revt -> {reverse_time()}')

main()
