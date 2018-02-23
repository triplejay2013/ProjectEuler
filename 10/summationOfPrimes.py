#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17
#Find the sum of all the primes below two million

#this sieve generates a list of primes up to a limit 'n'
#this is modeled after the sieve of eratosthenes
#Parameters:
#   n - the upper limit which must be greater than 2
#Return
#   primeList - a list of primes generated up to the limit n
def prime_sieve(n):
    #holds the values of prime #'s
    prime = [2,3]
    #numbers marked as non-prime - default set to True
    sieve = [True] * (n+1)
    #start at 2 and continue until the limit
    for i in xrange(2, n+1):
        #if i isn't in the marked list then it must be prime, according to the algorithm
        #of the sieve of aratosthenes
        if sieve[i]:
            #add number to primeList
            prime.append(i)
            #start at the square(according to algorithm) and continue until the limit,
            #skipping at intervals equal to multiples of i
            for j in xrange(i*i, n+1, i):
                sieve[j] = False
    return prime

def sum_primes(n, primes):
    total = 0
    while next(primes):
        total += primes[i]
    return total

primes = prime_sieve(10)
print("\ncalculating primes\n")
print(sum_primes(primes))
print("\nall done!\n")
