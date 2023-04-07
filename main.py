import argparse
import numpy as np
import random
from distribution import generate_random

# Assume number of family N=1000
# Assume size of each family ranging from 1 to 8

N = 1000
MIN = 1
MAX = 9
SAMPLE_NUM = 10
SAMPLE_TIME = 5

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', default='normal',
                        choices=['uniform', 'normal', 'left', 'right'], type=str)
    args = parser.parse_args()

    family_size = generate_random(args, MIN, MAX, N)
    people = []
    for size in family_size:
        for _ in range(int(size)):
            people.append(int(size))

    # print(family_size)
    # print(people)
    random.shuffle(people)

    sum = 0
    for i in range(SAMPLE_TIME):
        idices = random.sample(range(0, len(people)), SAMPLE_NUM)
        sum_per_time = 0
        for idx in idices:
            sum_per_time += people[idx]
        sum += sum_per_time
        print("Iteration", i, ":", sum_per_time/SAMPLE_NUM)

    print("="*20)
    print("MODE:", args.mode)
    print("Predict average family size:", sum/(SAMPLE_TIME*SAMPLE_NUM))
    print("Truth average family size:", np.array(family_size).mean())
    print("Total population:", len(people))
