import random
def gcd(x, y): # 유클리드 알고리즘을 이용한 x,y의 최대값 찾는 함수
    r = x%y # 나머지 값 r 저장
    while (r != 0): # 나머지값인 r이 0이 될때까지 반복
        x = y 
        y = r
        r = x%y
    return int(y) # 유클리드 알고리즘의 결과인 최대공약수 return


def extend_gcd(x,y): # extended gcd
    s1,s2=1,0 # 초기 s1,s2 값 설정
    t1,t2=0,1 # 초기 t1,t2 값 설정
    while(1): # x=q*y+r
        q=x//y
        r=x-(q*y)
        s=s1-(q*s2)
        t=t1-(q*t2)

        if r==0: # 나머지 값인 r이 0인 경우 s2,t2가 s,t 값임으로 return
            return s2
        
        # 다음 연산을 위한 x,y,s1,s2,t1,t2 값 세팅
        x=y
        y=r
        s1=s2
        s2=s
        t1=t2
        t2=t

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

def rsa_genkey(key_length): # PK,SK 생성 함수
    e=65537 # 지수값은 가장 많이 쓰이는 65537로 설정
    while(1): # 해당조건을 만족하는 p를 찾을 때까지 계속 반복
        p=random.getrandbits(key_length)
        if is_prime(p) and (gcd(e,p-1)==1): # 조건을 만족하는 p를 찾으면 break
            break
    while(1): # 해당조건을 만족하는 q를 찾을 때까지 계속 반복
        q=random.getrandbits(key_length)
        if is_prime(q) and (gcd(e,q-1)==1): # 조건을 만족하는 p를 찾으면 break
            break
    n=p*q
    pi=(p-1)*(q-1) 
    d=extend_gcd(e,pi)%pi # d=e의 역원, 따라서 extend_gcd를 이용해서 e의 역원을 구한다.
    pk=n,e # PK(n,e)
    sk=p,q,d # SK(p,q,d)
    return pk,sk       

def rsa_encrypt(m,pk): # encrypt 함수
    n,e=pk
    ct=mod_exp(m,e,n) # PK를 통해 받은 e,n 그리고 메시지 m을 modexp하여 암호문 생성
    return ct

def rsa_decrypt(ct,sk): # decrypt 함수
    p,q,d=sk 
    n=p*q
    m=mod_exp(ct,d,n) # SK를 통해 받은 p,q,d 그리고 암호문 ct를 modexp하여 메시지 복호화
    return m

m=17011634
# 1024비트
pk,sk=rsa_genkey(1024) 
print('PK: ',pk)
print('SK: ',sk)
ct=rsa_encrypt(m,pk)
pt=rsa_decrypt(ct,sk)
print("1024 encrypt result: ",ct)
print("1024 decrypt result: ",pt)
print()
# 512비트
pk,sk=rsa_genkey(512)
print('PK: ',pk)
print('SK: ',sk)
ct=rsa_encrypt(m,pk)
pt=rsa_decrypt(ct,sk)
print("512 encrypt result: ",ct)
print("512 decrypt result: ",pt)
print()
# 256비트
pk,sk=rsa_genkey(256)
print('PK: ',pk)
print('SK: ',sk)
ct=rsa_encrypt(m,pk)
pt=rsa_decrypt(ct,sk)
print("256 encrypt result: ",ct)
print("256 decrypt result: ",pt)