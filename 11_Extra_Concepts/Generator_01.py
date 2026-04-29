# Print Prime numbers using generators  

def gen_primes(start, end):
    for num in range(start, end + 1):
        if num < 2:
            continue
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
            
for prime in gen_primes(50, 1000):
    print(prime)