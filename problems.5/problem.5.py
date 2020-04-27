def is_prime(num):
    if num <= 3:
        return True
    for i in range(num//2, 1, -1):
        if num % i == 0:
            return False 
    return True

_from, _to = 1, 20
primes = list(filter(lambda x: is_prime(x), range(_from+1, _to+1)))

all_factors_by_value = []
for i in range(_from+1, _to+1):
    num = i
    factors = []
    for prime in primes:
        if num>=prime:
            while num % prime == 0:
                num //= prime
                factors.append(prime)
    all_factors_by_value.append((factors))

print("\n"*2,"Factors,")
for index, factor_list in enumerate(all_factors_by_value):
    print("{:<3} {}".format(index+2, factor_list))

# Max counts of primes in factor lists
print("_"*20, "\n ", "Max primes in factor lists")
count_of_primes = {}
for prime in primes:
    count_of_primes[str(prime)] = max(list(map(lambda x: x.count(prime), all_factors_by_value)))
    print("{:<3} count: {}".format(prime, count_of_primes[str(prime)]))

product = 1
for prime, count in count_of_primes.items():
    product *= int(prime)**count

print("\n>> Smallest multiple is", product)

