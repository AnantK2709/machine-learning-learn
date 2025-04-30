import multiprocessing
import math
import time
import sys

sys.set_int_max_str_digits(10000000)

def compute_factorial(n):
    print(f"Computing factorial of {n}")
    result = math.factorial(n) 
    print(f"Factorial of {n} is {result}")
    return result

if __name__ == "__main__":
    numbers = [5000,6000,7000,8000,9000,10000]
    results= []
    start_time = time.time()
    with multiprocessing.Pool() as pool:
        results = pool.map(compute_factorial, numbers) #Time taken: 0.21743392944335938 seconds
    # for i in numbers:
    #     results.append(compute_factorial(i)) Time taken: 0.06834101676940918 seconds
    end_time = time.time()
    print(f"Results: {results}")
    print(f"Time taken: {end_time - start_time} seconds")
# This script demonstrates how to compute the factorial of multiple numbers concurrently using multiprocessing.