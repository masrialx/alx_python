def fibonacci_sequence(n):
    sequence = []
    
    if n <= 0:
        return sequence
    
    elif n == 1:
        sequence.append(0)
        return sequence
    
    elif n == 2:
        sequence.extend([0, 1])
        return sequence
    
    else:
        sequence.extend([0, 1])
        for i in range(2, n):
            next_number = sequence[i-1] + sequence[i-2]
            sequence.append(next_number)
        
        return sequence
n = 10
fibonacci_numbers = fibonacci_sequence(n)
print(fibonacci_numbers)
