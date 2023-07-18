def is_prime(number):
    if number < 2:
        return False
    
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    
    return True
num = 17
is_num_prime = is_prime(num)
print(is_num_prime)
