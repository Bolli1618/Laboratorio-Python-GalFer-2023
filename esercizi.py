# FUNZIONI E CONDIZIONI

def divisibile_per_17(n) -> bool:
    if n % 17 == 0:
        return True
    else:
        return False

print(divisibile_per_17(15))
print(divisibile_per_17(34))

# LISTE

lista = ["Lorem", "ipsum", "dolor", "sit", "amet"]
print(lista)

def scambia(lista):
    a = lista[0]
    b = lista[-1]
    lista[0] = b
    lista[-1] = a

scambia(lista)
print(lista)

# CICLI

def valutazione_padica(p, n) -> int:
    k = 0
    while n % p**(k+1) == 0:
        k = k + 1

    return k

print(valutazione_padica(3, 324))

# FIBONACCI

def fibonacci(n):
    numeri = [0, 1]
    
    for i in range(n):
        if i > 1:
            numeri.append(numeri[i-2]+numeri[i-1])
    
    return numeri

print(fibonacci(20))

# NUMERI AMICI

def divisors_sum(n):
    divisors = []
    for i in range(n):
        if i != 0 and n % i == 0:
            divisors.append(i)
    
    return sum(divisors)


def areFriendNumbers(n1, n2):
    if divisors_sum(n1) == n2 and divisors_sum(n2) == n1:
        return True
    else: return False

print(areFriendNumbers(18416, 17296))
