import random

def mod_exp(a,e,n): # modexp
    s = 1
    r = 0
    exp = bin(e) # 지수 값인 e를 binary 값으로 변환
    for i in range(2,len(exp)): # 2진수로 표현된 binary를 왼쪽부터 하나씩 스캔
        if(exp[i:i+1] == '1'): # i번째 바이너리 비트가 1인 경우
            r = (s*a) % n # multiple
        else:
            r = s
        s = (r*r) % n # square
    return r
    
def miller_test(n,b,s,t): # Miller-Rabin Test
    a = mod_exp(b,t,n) # (b,t,n)을 modexp 해줌으로써 b ^ t를 mod n한 결과를 반환
    if a == 1 or a == n-1: # 첫 modexp의 결과가 1 or -1이면 소수임으로 return 1
        return 1
    for i in range(0,s): # 0 ~ s-1만큼 cycle 반복
        a = mod_exp(a,2,n) # (a ^ 2) mod n 결과 return
        if a == 1: # 결과가 1이면 합성수 -> return 1
            return 0
        elif a == n-1: # 결과가 -1이면 소수 -> return 1
            return 1
    return 0 # 반복문을 모두 반복했다면, 최종 결과는 합성수 -> return 0    
  
def is_prime_miller_rabin(n):
    count = 0 # Miller-Rabin Test 성공 횟수 counting
    s = 0
    t = n-1
    while t % 2 == 0: # n-1 = (2 ^ s)*t 로 변환하는 과정
        t = t>>1
        s += 1
  
    for i in range(30):
        b = random.randrange(2,n) # 2 ~ n중 랜덤 b 선택
        if miller_test(n,b,s,t) == 1: # Miller-Rabin Test 결과가 소수면
            count += 1 # count 증가
    if count > 20: # `Miller-Rabin Test 결과 == 참`이 20 케이스 이상인 경우
        return 1 # 소수로 판정하고 return 1
    else:
        return 0 # 합성수로 판정하고 return 0
  
print(is_prime_miller_rabin(561))
print(is_prime_miller_rabin(563))
print(is_prime_miller_rabin(2 ** (2 ** 4) + 1))
print(is_prime_miller_rabin(2 ** (2 ** 5) + 1))
print(is_prime_miller_rabin(2 ** 1279 - 1))
print(is_prime_miller_rabin(2 ** 1279 + 1))
print(is_prime_miller_rabin(2 ** 3217 - 1))
