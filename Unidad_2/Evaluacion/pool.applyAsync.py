import multiprocessing as mp
import numpy as np
from time import time

np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
data[:5]

pool = mp.Pool(mp.cpu_count())
results = []


def howmany_within_range2(i, row, minimum, maximum):
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return (i, count)


def collect_result(result):
    global results
    results.append(result)


for i, row in enumerate(data):
    pool.apply_async(howmany_within_range2, args=(
        i, row, 4, 8), callback=collect_result)

pool.close()

print(results_final[:10])
