# 최대공약수(GCD) & 최소공배수(LCM)

n1, n2 = map(int, input().split())

def gcd(n1, n2):
  na = max(n1, n2)
  nb = min(n1, n2)
  
  while na % nb != 0:
    temp = na % nb # 24 18 6
    na = nb
    nb = temp # 18 6

  return nb

def lcm(n1,n2):
  return (n1 * n2) // gcd(n1, n2)

  

  
print(gcd(n1, n2))
print(lcm(n1, n2))
