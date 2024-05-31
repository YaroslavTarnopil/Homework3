import time
from multiprocessing import Pool, cpu_count

def factorize(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def parallel_factorization(numbers):
    with Pool(cpu_count()) as pool:
        results = pool.map(factorize, numbers)
    return results

if _name_ == "_main_":
    numbers = [12345678, 98765432, 34567890, 54321098]

    start_time = time.time()
    parallel_factorization(numbers)
    end_time = time.time()

    print(f"Parallel execution time: {end_time - start_time} seconds")