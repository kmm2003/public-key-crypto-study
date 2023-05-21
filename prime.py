import random
def mod_exp(a,e,n): # modexp
    s=1
    r=0
    exp=bin(e) # 지수 값인 e를 binary 값으로 변환
    for i in range(2,len(exp)): # 2진수로 표현된 binary를 왼쪽부터 하나씩 스캔
        if(exp[i:i+1]=='1'): # i번째 바이너리 비트가 1인 경우
            r=(s*a)%n # multiple 연산
        else:
            r=s
        s=(r*r)%n # square 연산
    return r
    
def miller_rabin_test(n,b,s,t): # Miller-Rabin Test
    a=mod_exp(b,t,n) # (b,t,n)을 modexp 해줌으로써 b의 t제곱을 mod n한 결과를 반환
    if a==1 or a==n-1: # 첫 modexp의 결과가 1 or -1이면 소수임으로 1 return
        return 1
    for i in range(0,s): # 0~s-1번까지 cycle 반복
        a=mod_exp(a,2,n) # a값에 제곱한 값을 mod n 한 결과 반환
        if a==1: # 결과가 1이면 합성수임으로 0 return
            return 0
        elif a==n-1: # 결과가 -1이면 소수임으로 1 return
            return 1
    return 0 # 반복문을 모두 반복했다면 최종 결과는 합성수임으로 0 return                                   
        
def is_prime(n):
    count=0 # Miller-Rabin Test 성공 횟수 counting
    s=0
    t=n-1
    while t%2==0: # n-1=(2의 s제곱)*t로 변환하는 과정
        t=t>>1
        s+=1
  
    for i in range(30):
        b=random.randrange(2,n) # 2~n중 랜덤 b값 선택
        if miller_rabin_test(n,b,s,t)==1: # Miller-Rabin Test의 결과가 소수이면
            count+=1 # count 증가
    if count > 20: # Miller-Rabin Test 결과가 참인 경우가 20 케이스 이상인 경우
        return 1 # 소수로 판정하고 1 return
    else:
        return 0 # 합성수로 판정하고 0 return
    
print('a)',is_prime(561))
print('b)',is_prime(569))
print('c)',is_prime(2 ** (2 ** 4) + 1))
print('d)',is_prime(2 ** (2 ** 10) + 1))
print('e)',is_prime(2 ** 1279 - 1))
print('f)',is_prime(2 ** 2203 - 1))
print('g)',is_prime(2 ** 3217 - 1))