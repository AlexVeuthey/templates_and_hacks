import time
import datetime
from progress.bar import Bar

# ################################
# ESTIMATED TIME OF ARRIVAL (ETA) FOR PROCESSING LONG LISTS
# ################################


def main():
    items = range(10000)

    t_start = time.time()
    t_total = 0.0
    n = 0

    bar = Bar('Processing', max=len(items))

    for _ in items:
        t_current = time.time() - t_start
        t_start = time.time()
        t_total += t_current
        n += 1

        mean = t_total / n
        remaining = int((len(items) - n) * mean)

        bar.next()

        # print should be after bar.next(), so that we still see the mean time per item after end of loop
        print(' Mean: {0:.2f}ms ETA: {1:0>8}'.format(1000 * mean, str(datetime.timedelta(seconds=remaining))), end='',
              flush=True)
    bar.finish()


if __name__ == '__main__':
    main()
