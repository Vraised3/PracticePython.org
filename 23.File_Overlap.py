with open('primenumbers.txt', 'r') as prime_nums:
    primes = prime_nums.read()

with open('happynumbers.txt', 'r') as happy_nums:
    happy = happy_nums.read()

primes = list(map(int, primes.split()))  # Convert to int
happy = list(map(int, happy.split()))

same = [a for a in primes if(a in happy)]

print(same)
