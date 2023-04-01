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