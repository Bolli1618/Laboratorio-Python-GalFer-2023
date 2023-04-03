# Esercizi e Soluzioni

## Funzioni e condizioni:

- Crea una funzione che prende in argomento un numero e ritorna True se è divisibile per 17, False se non lo è. Verifica che funzioni chiamandola per 15 e 34, printando il risultato. **Hint:** prova a usare l'operatore modulo "```%```"

**Soluzione:**
``` python
def divisibile_per_17(n) -> bool:
    if n % 17 == 0:
        return True
    else:
        return False

print(divisibile_per_17(15))
print(divisibile_per_17(34))
```

## Liste

- Crea una lista di almeno 4 elementi e printala, poi crea una funzione che prende in argomento una lista e ne scambia il primo e l'ultimo elemento. Chiama la funzione e printane il risultato.
**Hint:** In una lista ```l``` puoi usare la notazione ```l[-1]``` per selezionare l'ultimo elemento di ```l```

**Soluzione:**
``` python
lista = ["Lorem", "ipsum", "dolor", "sit", "amet"]
print(lista)

def scambia(lista):
    a = lista[0]
    b = lista[-1]
    lista[0] = b
    lista[-1] = a

scambia(lista)
print(lista)
```

## Cicli

- (Valutazione p-adica) Crea una funzione che prende in argomento due numeri e trova il più grande esponente al quale il primo divide il secondo.
Controlla se funziona cercando la massima potenza di 3 che divide 324
**Procedimento:**
    - Definisci la funzione che prende in argomento p, n
    - inizializza una variabile k, l'esponente di p, inizialmente 0
    - inizia un ciclo che prosegue fintanto che n è divisibile per p^(k+1), durante il quale fa aumentare k di 1
    - ritorna k
    - chiama la funzione su 3, 324

**Solunzione:**
``` python
def valutazione_padica(p, n) -> int:
    k = 0
    while n % p**(k+1) == 0:
        k = k + 1

    return k

print(valutazione_padica(3, 324))
```

## Fibonacci

- Crea una funzione che trova i primi n numeri della sequenza di fibonacci e testala sui primi 20. **Procedimento:**
    - Definisci una funzione che prende come argomento n, cioè quanti numeri di Fibonacci verranno calcolati
    - Inizializza una lista contente 0, 1
    - Avvia un ciclo for che itera la variabile i nei numeri da uno a n. Questo aggiungerà alla lista l'i-esimo numero di Fibonacci, dopo aver verificato che i sia maggiore di 1
    - ritorna la lista
    - chiama la funzione con parametro 20 per verificare che funzioni

**Soluzione:**
``` python
def fibonacci(n):
    numeri = [0, 1]
    
    for i in range(n):
        if i > 1:
            numeri.append(numeri[i-2]+numeri[i-1])
    
    return numeri

print(fibonacci(20))
```
