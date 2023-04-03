# FUNZIONI E CONDIZIONI

def divisibile_per_17(n):
    # controlla che il resto della divisione per 17 sia 0
    if n % 17 == 0:
        # se è 0, allora il numero è divisibile
        # per 17, ritorna True 
        return True
    else:
        # altrimenti non lo è, ritorna False
        return False

print(divisibile_per_17(15)) # False
print(divisibile_per_17(34)) # True

# LISTE

lista = ["Lorem", "ipsum", "dolor", "sit", "amet"]
print(lista) # ["Lorem", "ipsum", "dolor", "sit", "amet"]

def scambia(lista):
    # memorizza il primo elemento della lista
    a = lista[0]
    # memorizza l'ultimo elemento della lista
    b = lista[-1]
    
    # posiziona l'ultimo elemento al posto del primo
    lista[0] = b
    # posiziona il primo elemento al posto dell'ultimo
    lista[-1] = a

scambia(lista)
print(lista) # ["amet", "ipsum", "dolor", "sit", "Lorem"]

# CICLI

def valutazione_padica(p, n):
    # imposta la variabile k (esponente) a 0
    k = 0
    # finchè n è divisibile per p**(k+1) 
    while n % p**(k+1) == 0:
        # aggiungi 1 a k
        k = k + 1

    # alla fine ritona k
    return k

print(valutazione_padica(3, 324)) # 4

# FIBONACCI

def fibonacci(n) -> List[int] :
    # crea una lista contenete i primi 2 numeri della sequenza
    numeri = [0,1]

    # ripeti n volte
    for i in range(n):
        # se l'indice di ripetizione è maggiore di 1
        if i > 1:
            # il numero successivo è la somma dei due precedenti
            numeri.append(numeri[i-2] + numeri[i-1])
    
    # ritorna la lista di numeri
    return numeri

print(fibonacci(10)) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# NUMERI AMICI

def divisors_sum(n):
    # crea una lista in cui metteremo i divisori di n
    divisors = []
    # ripeti n volte
    for i in range(n):
        # se l'indice di ripetizione è diverso da 0
        # e se n è divisibile per l'indice
        if i != 0 and n % i == 0:
            # aggiungi i alli sui divisori
            divisors.append(i)
    
    # ritorna una somma dei divisori
    return sum(divisors)

# controlla se due numeri sono amici
def are_friend_numbers(n1, n2):
    # se uno è la somma dei divisori dell'altro
    if divisors_sum(n1) == n2:
        # ritorna True
        return True
    else: 
        # altrimenti ritorna False
        return False

print(are_friend_numbers(18416, 17296)) # True
