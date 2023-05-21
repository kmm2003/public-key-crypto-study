import random
import hashlib
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

def generate_prime_subgroup(plen,glen): # p,q,g,A 생성 함수
    chk=1
    while(chk): # 해당조건을 만족하는 p를 찾을 때까지 계속 반복
        q=random.getrandbits(glen)
        if is_prime(q): # q가 소수인지 체크
            k=random.getrandbits(plen) # p의 길이가 plen이어야 함으로 k를 plen 길이의 임의의 정수로 생성 
            while(1):
                p=q*k+1 
                if is_prime(p): # 생성한 p값이 소수인지 체크
                    chk=0
                    break
            
    a=random.randrange(2,p) # 1 < a < p 인 a 생성
    g=mod_exp(a,k,p) # 생성한 p와 a를 이용하여 g 생성
    A=pow(g,a) # g,a를 이용해 A 생성
    return [p,q,g,A] # PK 값인 p,q,g,A return

def schnorr_setup(plen): # generate_prime_subgroup을 통해 구한 PK를 return
    pp=generate_prime_subgroup(plen,160)
    return pp

def schnorr_genkey(pp): # 받은 p,q,g,A와 랜덤 SK 값을 생성하여 PK, SK 생성 
    p,q,g,A=pp
    PK=pp
    SK=random.randrange(0,q-2)
    return SK,PK

def schnorr_hash(R,msg,q): # msg를 해싱하고 R, q 값을 이용해 h값을 생성
    enc=hashlib.md5()
    msg=msg.encode('utf-8')
    enc.update(msg)
    msg_enc=enc.hexdigest() 
    h=mod_exp(R/int(msg_enc,16),1,q)
    return h

def schnorr_sign(msg,sk,pp): # SK를 이용해 msg signing
    p,q,g,A=pp
    r=random.randrange(0,q-2)
    R=mod_exp(g,r,p)
    h=schnorr_hash(R,msg,q) # msg를 해싱하고 h값 생성
    s=mod_exp(r+sk*h,1,q)
    return [R,s] # 구한 R,s 값을 return

def schnorr_verify(sig, msg, pk, pp): # PK와 sig를 통해 정상적으로 서명이 됐는지 체크
    p,q,g,A=pk
    R,s=sig
    h=schnorr_hash(R,msg,q)
    if pow(g,s)==pow(R*pow(A,h)): # 두 값이 일치하면 서명이 정상적인 것으로 판단
        return 1
    return 0

plen = 256
pp = schnorr_setup(plen)
sk, pk = schnorr_genkey(pp) 
msg = 'This is a text message'
sig = schnorr_sign(msg, sk, pp)
print(schnorr_verify(sig, msg, pk, pp))

plen = 512
pp = schnorr_setup(plen)
sk, pk = schnorr_genkey(pp) 
msg = 'This is a text message'
sig = schnorr_sign(msg, sk, pp)
print(schnorr_verify(sig, msg, pk, pp))

plen = 1024
pp = schnorr_setup(plen)
sk, pk = schnorr_genkey(pp) 
msg = 'This is a text message'
sig = schnorr_sign(msg, sk, pp)
print(schnorr_verify(sig, msg, pk, pp))

plen = 2048
pp = schnorr_setup(plen)
sk, pk = schnorr_genkey(pp) 
msg = 'This is a text message'
sig = schnorr_sign(msg, sk, pp)
print(schnorr_verify(sig, msg, pk, pp))