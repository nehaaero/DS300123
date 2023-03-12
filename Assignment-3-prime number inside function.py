def is_prime(n):
    """Return true if n is prime, else False."""
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
def twin_primes(n):
        """print twin primes less than n."""
        for i in range(3, n-1, 2):
            if is_prime(i) and is_prime(i+2):
                print(i,"and",i+2)
twin_primes(20)


