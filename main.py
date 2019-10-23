import time
import statistics

INTERFACE = 'wlp3s0'

measurements = []

UPDATES_PER_SECOND = 5
AVERAGE_WINDOW = 20


def update_measurements():
    with open('/proc/net/wireless') as wireless_handle:
        lines = wireless_handle.readlines()
        last_line = lines[-1]
        measurements.append(float(last_line.split()[2]))
        if len(measurements) > AVERAGE_WINDOW:
            measurements.pop(0)
    print_average()


def print_average():
    print('Average signal: {:.1f}'.format(statistics.mean(measurements)))


def main():
    while True:
        update_measurements()
        time.sleep(1.0 / UPDATES_PER_SECOND)


if __name__ == '__main__':
    main()
