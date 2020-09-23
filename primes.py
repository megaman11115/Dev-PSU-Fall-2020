def is_prime(a):
    b = 2
    c = 0
    while b < a:
        if a % b == 0:
            c += 1
        b += 1
    if c > 0:
        return False
    return True

def next_prime(a):
    a += 1
    while is_prime(a) is False:
        a += 1
    return a

def p_factorization(p):
    p_naught = 2
    f = []
    while p > 1:
        if p % p_naught == 0:
            p /= p_naught
            f.append(p_naught)
            p_naught = 2
        else:
            p_naught = next_prime(p_naught)
    return f

def gcd(a, b):
    while a % b != 0:
        a %= b
        temp = a
        a = b
        b = temp
    return b

def main():
    print(p_factorization(1092308))
    print(gcd(12, 10))
main()

