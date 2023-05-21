def gcd(x, y): # 유클리드 알고리즘을 이용한 x,y의 최대값 찾는 함수
    r = x%y # 나머지 값 r 저장
    while (r != 0): # 나머지값인 r이 0이 될때까지 반복
        x = y 
        y = r
        r = x%y
    return int(y) # 유클리드 알고리즘의 결과인 최대공약수 return

def phi(n): # 파이 연산 결과 출력함수
    phi_n = 1 # 1은 무조건 n과 서로소임으로 phi_n(서로소의 갯수)을 1로 시작
    i = 2
    while (i<n): # n이하의 정수중 n과 서로소인 소수의 갯수를 구하기 위해 i=2 부터 하나씩 확인
        r = gcd(n, i) # gcd 연산을 통해 최대공약수를 구함
        i = i + 1
        if(r==1): # r==1 즉, n과 i가 서로소 이면 phi_n 을 상승
            phi_n = phi_n + 1
    return phi_n # phi(n) 값 retrun

def mod_exp(a,e,n):
    if e>100000: # 지수 값이 100000 이상인 경우에는 연산이 오래걸리기 때문에 파이 연산을 통해 e값을 감소
        e=e%phi(n)

    exp=bin(e) # 지수 값인 e를 binary 값으로 변환
    value=a

    for i in range(3,len(exp)): # 2진수로 표현된 binary를 왼쪽부터 하나씩 스캔
        value=value*value # square 연산
        if(exp[i:i+1]=='1'): # 바이너리 비트 값이 1이면 추가로 multiply 연산 수행
            value=value*a
    
    return f'{value%n} mod {n}' # 최종 결과 출력


def extend_gcd(x,y): # extended gcd
    s1,s2=1,0 # 초기 s1,s2 값 설정
    t1,t2=0,1 # 초기 t1,t2 값 설정
    if x < y:
        x,y=y,x

    while(1): # x=q*y+r
        q=x//y
        r=x-(q*y)
        s=s1-(q*s2)
        t=t1-(q*t2)

        if r==0: # 나머지 값인 r이 0인 경우 s2,t2가 s,t 값임으로 return
            return s2,t2
        
        # 다음 연산을 위한 x,y,s1,s2,t1,t2 값 세팅
        x=y
        y=r
        s1=s2
        s2=s
        t1=t2
        t2=t

def crt(p,q,a,b): # x=a mod p and x=b mod q
    value=p*q
    s,t=extend_gcd(p,q) # extended gcd를 통해 s,t 값을 계산
    x=a*s*q+b*t*p # 구한 s,t 값을 이용하여 x 값 계산
    while(x<0): # x값이 음수인 경우 양수로 변환
        x=x+value
    return x%value # crt 연산 최종 결과 출력!

def crt_list(p,v): # x=v[i] mod p[i]
    sum=p[0]*p[1]*p[2]
    u=list()
    for i in p:
        N=sum//i
        s,t=extend_gcd(N,i) # extend_gcd를 통해 N*u[i]= 1 mod p[i]에서의 u[i]를 구한다.
        u.append(s)

    # 윗 과정에서 구한 u값, p[i]에 대한 N값, v[i]을 각각 곱해 모두 더함
    result=v[0]*(sum/p[0])*u[0]+v[1]*(sum/p[1])*u[1]+v[2]*(sum/p[2])*u[2]
    result=result%sum # result 값을 sum로 나누면 우리가 원하는 crt_list의 결과 값이 나옴
    return int(result)



print('a)',mod_exp(3,12345,97))
print('b)',mod_exp(3,123456789012345,976))
print('c)',crt(10,21,1,2))
print('d)',crt(257,293,11,13))
print('e)',crt_list([10,21,29],[1,2,3]))
print('f)',crt_list([257,293,337],[11,13,31]))