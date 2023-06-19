import random
def is_prime(n):
  if n < 2:
    return 0
  for i in range(2, n):
    if i > (n/i): # i가 n/i보다 큰 경우까지 합성수 판정을 못받았다면 무조건 소수임으로 return 1
        return 1
    if n % i == 0: # i|n이 성립함으로 합성수
        return 0
  return 1

# is_prime()을 통해 2 ~ n의 숫자를 모두 소수인지 판별하고 출력
def generate_all_primes(n): 
  arr = []
  for i in range(2, n+1):
    if is_prime(i):
      arr.append(i)
  return arr 

# generate_all_primes()와 원리는 동일하나 s ~ e의 숫자를 대상으로만 소수 판별하고 랜덤 index를 지정해서 1개만 출력
def generate_random_prime(s, e): 
  arr = []
  for i in range(s, e+1):
    if is_prime(i):
      arr.append(i)
  index = random.randrange(len(arr))
  return arr[index]

print("-"*20+"is_prime"+"-"*20)
print(is_prime(11))
print(is_prime(253))
print(is_prime(65537))
print("-"*20+"generate_all_primes"+"-"*20)
print(generate_all_primes(50))
print(generate_all_primes(100))
print(generate_all_primes(1000))
print("-"*20+"generate_random_prime"+"-"*20)
print(generate_random_prime(2, 11))
print(generate_random_prime(100, 200))
print(generate_random_prime(1000, 2000))