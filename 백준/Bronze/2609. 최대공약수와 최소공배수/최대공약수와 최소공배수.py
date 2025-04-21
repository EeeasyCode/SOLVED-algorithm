a, b = map(int, input().split())

def gcd(a, b):
    # 탈출 조건
    if a%b==0: return b

    # 재귀
    return gcd(b, a%b)

def lcm(a, b):
  g = gcd(a, b)
  return g * (a//g) * (b//g)

print(gcd(a, b))
print(lcm(a, b))