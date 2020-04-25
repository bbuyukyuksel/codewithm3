import numpy as np
import threading
import time
import os
s_time = time.time()

number = 77   
from_half = number // 2

# Thread Configs
thread_num = 32
pool_answers = [0] * (thread_num - 1)
pool_current_nums = [0] * (thread_num - 1)
isResultObserverThreadDone = False

def is_prime(num):
    for i in range(num//2, 2, -1):
        if num % i == 0:
            return False 
    return True

def LPF(index, number, _from, _to):
    for _,i in enumerate(range(_from, _to, -1)):
        pool_current_nums[index] = i
        if number % i == 0:
            if is_prime(i):
                pool_answers[index] = i
                break

def result_observer():
    while not isResultObserverThreadDone:
        os.system('cls')
        print("Current Results,", pool_answers)
        print("Current  Values,", pool_current_nums)
        time.sleep(1)

# split steps for smaller workpieces
steps = [int(x) for x in np.linspace(from_half, 1, thread_num)]

# Append threads to pool
thread_list = []
for index, i in enumerate(range(len(steps)-1)):
    _from, _to =  steps[i:i+2]
    print("Thread append to Pool {:<3}, From {:<15} to {:<15}".format(index, _from, _to))
    thread_list.append(threading.Thread(target=LPF, args=(index, number, _from, _to)))
    thread_list[-1].name = f"Pool Index:{index}"

# Start threads
print('_'*20)
for thread in thread_list:
    print(f"(!) Started pool, name: {thread.name}")
    thread.start()

# Start result observer thread
threading.Thread(target=result_observer).start()

# Wait to join
for thread in thread_list:
    thread.join()

# Disabled observer thread
isResultObserverThreadDone = True
# Wait to stop observer thread
time.sleep(1)

result = list(filter(lambda x: x!=0, pool_answers))[0]
print("Calculated for ", number)
print("\n", u'\u2713', "Largest Prime Factor is ", result)
print("Elapsed time", time.time() - s_time, "seconds")