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

# lucas lehmer test
def lucas_lehmer_test(p):
  n = 2 ** p - 1 # Mp 계산
  r = 4 #  r1
  for i in range(2, p): # k >= 2
    # p-1 까지 계산
    r = (r**2 - 2) % n
  if r == 0: # 결과가 0이면 Mersenne Prime으로 판단
    return 1
  return 0

def find_mersenne_primes(max):
  # 1 ~ max까지 모든 prime을 찾음
  arr = generate_all_primes(max)
  result = []
  for prime in arr: # 찾은 prime 마다 lucas lehmer test 수행
    if lucas_lehmer_test(prime):
      # 결과가 참이면 prime 저장
      result.append(prime)
  return result

print(lucas_lehmer_test(5))
print(lucas_lehmer_test(17))
print(lucas_lehmer_test(31))
print(lucas_lehmer_test(521))
print(lucas_lehmer_test(9689))
print(lucas_lehmer_test(9697))
print(find_mersenne_primes(5000))