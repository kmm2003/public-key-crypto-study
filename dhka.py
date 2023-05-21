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

def dhka_genparams(prime_length): # p,g 생성 함수
    while(1): # 해당조건을 만족하는 p를 찾을 때까지 계속 반복
        q=random.getrandbits(prime_length)
        if is_prime(q): # q가 소수인지 체크
            p=q*2+1 
            if is_prime(p): # 생성한 p값이 소수인지 체크
                break
    a=random.randrange(2,p-1) 
    g=mod_exp(a,2,p) # 생성한 p와 a를 이용하여 g 생성
    return [p,g] # p,g 파라미터 return

def dhka_genkey(param): # PK, SK 생성 함수
    sk=random.randrange(1,param[0]-2) # 랜덤값 SK 생성
    pk=mod_exp(param[1],sk,param[0]) # param 내의 p,g 값을  이용하여 modexp 연산을 통해 PK 생성
    return sk,pk

def dhka_agree(sk, pk, param): # PK, SK를 modexp 연산하여 최종 비밀키 생성
    return mod_exp(pk,sk,param[0])

# 256 length
prime_length = 256
param = dhka_genparams(prime_length)
sk_a, pk_a = dhka_genkey(param)
sk_b, pk_b = dhka_genkey(param)
ek_a = dhka_agree(sk_a, pk_b, param)
ek_b = dhka_agree(sk_b, pk_a, param)

print('256 length')
print('ek_a: ', ek_a)
print('ek_b: ', ek_b)
print()

# 512 length
prime_length = 512
param = dhka_genparams(prime_length)
sk_a, pk_a = dhka_genkey(param)
sk_b, pk_b = dhka_genkey(param)
ek_a = dhka_agree(sk_a, pk_b, param)
ek_b = dhka_agree(sk_b, pk_a, param)

print('512 length')
print('ek_a: ', ek_a)
print('ek_b: ', ek_b)
print()

# 768 length
prime_length = 768
param = dhka_genparams(prime_length)
sk_a, pk_a = dhka_genkey(param)
sk_b, pk_b = dhka_genkey(param)
ek_a = dhka_agree(sk_a, pk_b, param)
ek_b = dhka_agree(sk_b, pk_a, param)

print('768 length')
print('ek_a: ', ek_a)
print('ek_b: ', ek_b)