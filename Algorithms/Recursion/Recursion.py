def sum_of_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_of_list(lst[1:])

arr=[2,4,6]
print(sum_of_list(arr))

def to_string(n,base):
    if n < base:
        return str(n)
    else:
        return to_string(n // base, base) + str(n % base)

print(to_string(15,2))

def sum_of_nested_list(lst):
    total = 0
    for item in lst:
        if isinstance(item, list):
            total += sum_of_nested_list(item)
        else:
            total += item
    return total

print(sum_of_nested_list([1, 2, [3,4], [5,6]]))

def factorial(num):
    if num <0:
        return
    elif num==0:
        return 1
    return num*factorial(num-1)

print(factorial(10))

def fibonnacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnacci(n - 1) + fibonnacci(n - 2)

print(fibonnacci(10))

def sumDigits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sumDigits(n // 10)

print(sumDigits(12345))

def sum_of_series(n):
    if n<=0:
        return 0
    else:
        return n + sum_of_series(n-2)
    
print(sum_of_series(10))

def harmonic_sum(n):
    if n <= 0:
        return 0
    else:
        return 1/n + harmonic_sum(n-1)

print(harmonic_sum(5))

def geometric_sum(n,r):
    if n <= 0:
        return 0
    else:
        return r**n + geometric_sum(n-1,r)

print(geometric_sum(5,2))

def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)
    
print(power(2, 3))