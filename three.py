# מבנה שפות תוכנה - תרגיל 3 

# name: Evyatar Baruch 
# I.D: 323916403

# name: Sapir Bashan
# I.D: 214103368




import sys
import time
import math

sys.setrecursionlimit(2000)

def create_tuple(n):
    """Creates a tuple with descending pairs (n, n-1) from n to 0 using regular recursion.
    
    This function meets the requirement by using standard recursion, where the complete tuple is built
    after all recursive calls are made.
    """
    if n <= 0:
        return ()  # Base case: returns an empty tuple when n reaches 0.
    return (n, n-1) + create_tuple(n - 2)  # Recursive call, updating the tuple at each stage.

result_regular = create_tuple(1000)

def create_tuple_tail(n, acc=()):
    """Creates a tuple with descending pairs from n to 0 using tail recursion with an accumulator.
    
    This function meets the requirement by accumulating the result in the accumulator (acc), which is
    passed through each recursive call, optimizing memory usage.
    """
    if n <= 0:
        return acc  # Base case: returns the accumulated tuple when n reaches 0.
    return create_tuple_tail(n - 2, acc + (n, n-1))  # Tail recursive call with updated accumulator.

result_tail = create_tuple_tail(1000)

def sum_tuple(tpl):
    """Calculates the sum of all elements in the tuple using regular recursion.
    
    This function meets the requirement by recursively summing each element of the tuple.
    """
    if not tpl:
        return 0  # Base case: returns 0 when the tuple is empty.
    return tpl[0] + sum_tuple(tpl[1:])  # Adds the first element with the recursive sum of the rest.

sum_regular = sum_tuple(result_regular)

def sum_tuple_tail(tpl, acc=0):
    """Calculates the sum of all elements in the tuple using tail recursion.
    
    This function meets the requirement by using an accumulator to hold the cumulative sum,
    passed through each recursive call.
    """
    if not tpl:
        return acc  # Base case: returns accumulated sum when the tuple is empty.
    return sum_tuple_tail(tpl[1:], acc + tpl[0])  # Tail recursive call with updated accumulator.

sum_tail = sum_tuple_tail(result_tail)

def gcd(a, b):
    """Calculates the greatest common divisor (GCD) of two numbers using regular recursion.
    
    This function meets the requirement by using Euclidean algorithm with a standard recursive call,
    returning the GCD.
    """
    if b == 0:
        return a  # Base case: returns `a` when `b` reaches 0.
    return gcd(b, a % b)  # Recursive call with modulus operation.

def lcm(a, b):
    """Calculates the least common multiple (LCM) of two numbers using the GCD function.
    
    This function meets the requirement by using the LCM formula which incorporates the GCD.
    """
    return abs(a * b) // gcd(a, b)  # Computes LCM using the GCD result.

lcm_regular = lcm(6, 4)

def gcd_tail(a, b):
    """Calculates the GCD of two numbers using tail recursion.
    
    This function meets the requirement by using the Euclidean algorithm with tail recursion,
    optimizing memory efficiency.
    """
    if b == 0:
        return a  # Base case: returns `a` when `b` is 0.
    return gcd_tail(b, a % b)  # Tail recursive call.

def lcm_tail(a, b):
    """Calculates the LCM of two numbers using the GCD function with tail recursion.
    
    This function meets the requirement by calculating the least common multiple with the tail-recursive GCD function.
    """
    return abs(a * b) // gcd_tail(a, b)  # Computes LCM using tail-recursive GCD.

lcm_tail_result = lcm_tail(6, 4)

def is_palindrome(n):
    """Checks if an integer is a palindrome using regular recursion.
    
    This function meets the requirement by recursively verifying that each pair of characters
    from both ends are identical in the string representation of the number.
    """
    s = str(n)
    if len(s) <= 1:
        return True  # Base case: returns True if only one or zero characters left.
    if s[0] != s[-1]:
        return False  # Returns False if the outermost characters are not equal.
    return is_palindrome(int(s[1:-1]))  # Recursive call with shortened string.

palindrome_regular = is_palindrome(123454321)

def is_palindrome_tail(n, s=None):
    """Checks if an integer is a palindrome using tail recursion.
    
    This function meets the requirement by using an accumulator `s` that stores the string representation
    of the number, enabling efficient comparison of characters from both ends.
    """
    s = str(n) if s is None else s  # Initialize `s` on first call.
    if len(s) <= 1:
        return True  # Base case: returns True if palindrome.
    if s[0] != s[-1]:
        return False  # Returns False if characters on both ends are not equal.
    return is_palindrome_tail(n, s[1:-1])  # Tail recursive call with shortened string.

palindrome_tail = is_palindrome_tail(123454321)

def sortedzip(*lists):
    """Sorts each list and returns the minimum of each list in a column-wise order.
    
    This function meets the requirement by creating a new list where each element is the minimum
    of each provided list.
    """
    if all(not lst for lst in lists):
        return []  # Base case when all lists are empty.
    mins = [min(lst) for lst in lists]  # List of minimums from each list.
    min_elems = tuple(mins)
    new_lists = [lst.remove(min(lst)) or lst for lst in lists]  # Removes minimum from each list.
    return [min_elems] + sortedzip(*new_lists)  # Recursive call with updated lists.

sortedzip_regular = sortedzip([3, 1, 2], [5, 6, 4], ['a', 'b', 'c'])

def sortedzip_tail(acc, *lists):
    """Sorts each list using tail recursion and stores the cumulative result in an accumulator `acc`.
    
    This function meets the requirement by accumulating the result in `acc`.
    """
    if all(not lst for lst in lists):
        return acc  # Base case when all lists are empty, returns sorted list.
    mins = [min(lst) for lst in lists]
    min_elems = tuple(mins)
    new_lists = [lst.remove(min(lst)) or lst for lst in lists]
    return sortedzip_tail(acc + [min_elems], *new_lists)  # Tail recursive call with updated accumulator.

sortedzip_tail_result = sortedzip_tail([], [3, 1, 2], [5, 6, 4], ['a', 'b', 'c'])

# Checking results by comparing function outputs in pairs
assert result_regular == result_tail
assert sum_regular == sum_tail
assert lcm_regular == lcm_tail_result
assert palindrome_regular == palindrome_tail
assert sortedzip_regular == sortedzip_tail_result

print("All tests passed!")  # Prints success message if all tests pass

# part 2

import sys
import time
import math

# 1. Generating a list without Lazy Evaluation
def create_full_array_eager():
    """Generates a full list eagerly by creating a list of integers from 0 to 10000.
    
    Meets the requirement by allocating memory immediately for the entire range.
    """
    return list(range(10001))

def create_partial_array_eager(full_array):
    """Creates a partial list by slicing the first 5000 elements from an eagerly evaluated list.
    
    Meets the requirement by creating a new list from the original array, consuming memory upfront.
    """
    return full_array[:5000]

# 2. Generating a list with Lazy Evaluation
def create_full_array_lazy():
    """Generates a full list lazily using a generator for numbers from 0 to 10000.
    
    Meets the requirement by using a generator, only evaluating each element as needed.
    """
    return (num for num in range(10001))

def create_partial_array_lazy(full_array):
    """Creates a partial generator that takes the first 5000 elements from a lazy evaluated sequence.
    
    Meets the requirement by avoiding upfront memory allocation and generating elements on demand.
    """
    return (next(full_array) for _ in range(5000))

# Measure time and memory without Lazy Evaluation
start_time = time.time()
full_array_eager = create_full_array_eager()
partial_array_eager = create_partial_array_eager(full_array_eager)
end_time = time.time()
print("Eager Evaluation - Full Array Time:", end_time - start_time)
print("Eager Evaluation - Full Array Memory:", sys.getsizeof(full_array_eager))  # Checks memory of full list.
print("Eager Evaluation - Partial Array Memory:", sys.getsizeof(partial_array_eager))  # Checks memory of partial list.
print("Eager Evaluation - Type Check:", type(full_array_eager) == type(partial_array_eager))  # Confirms type consistency.

# Measure time and memory with Lazy Evaluation
start_time = time.time()
full_array_lazy = create_full_array_lazy()
partial_array_lazy = create_partial_array_lazy(full_array_lazy)
end_time = time.time()
print("Lazy Evaluation - Full Array Time:", end_time - start_time)
print("Lazy Evaluation - Full Array Memory:", sys.getsizeof(full_array_lazy))  # Checks memory for generator (minimal).
print("Lazy Evaluation - Partial Array Memory:", sys.getsizeof(partial_array_lazy))  # Checks memory for partial generator.
print("Lazy Evaluation - Type Check:", type(full_array_lazy) == type(partial_array_lazy))  # Confirms type consistency.

# Prime number generator
def prime_generator():
    """Generates an infinite sequence of prime numbers using lazy evaluation.
    
    This meets the requirement for lazy evaluation, only producing the next prime when requested.
    """
    num = 2
    while True:
        is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))  # Checks if `num` is prime.
        if is_prime:
            yield num  # Yields the prime number, meeting lazy evaluation.
        num += 1

# Usage example for prime generator
gen = prime_generator()
print(next(gen))  # 2
print(next(gen))  # 3
print(next(gen))  # 5
print(next(gen))  # 7
print(next(gen))  # 11

# Taylor series generator for e^x
def taylor_series_e(x):
    """Generates the Taylor series approximation of e^x up to an infinite number of terms.
    
    This meets the requirement by computing each term on-demand, leveraging lazy evaluation.
    """
    n = 0
    total = 0
    while True:
        term = (x ** n) / math.factorial(n)  # Calculates the nth term of the series.
        total += term
        yield total  # Yields the cumulative total, representing an approximation of e^x.
        n += 1

# Usage example for Taylor series generator with x=2
gen = taylor_series_e(2)
for _ in range(8):
    print(next(gen))  # Prints successive approximations of e^2 using the series
