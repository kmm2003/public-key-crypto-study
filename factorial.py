import argparse
import sys

# Expend Depth
sys.setrecursionlimit(10**8)

def in_cache(func): # factorial result in cache dict
  cache = {}
  def wrapper(n):
    if n in cache:
      return cache[n]
    else:
      cache[n] = func(n)
      return cache[n]
  return wrapper

@in_cache
def factorial(n): # loop factorial algorithm
  return n * factorial(n-1) if n > 1 else 1

def binomial(n, k): # binomial algorithm with Used factorial alg
    return factorial(n) // (factorial(k) * factorial(n-k))

if __name__ == "__main__":
  parser = argparse.ArgumentParser()    
  parser.add_argument("n")
  parser.add_argument("k")
  args = parser.parse_args() # Input n and k
  # parsing int args
  n = int(args.n)
  k = int(args.k)
  inc = 1000
  if n > 1000: # if n > 1000 -> caching factorial result by 1000
    for i in range(1000, n+1, inc):
      factorial(i)
      inc = inc + i
  # Output result
  print("[+] factorial(n) :", factorial(n))
  print("[+] binomial(n,k) :", binomial(n, k))
