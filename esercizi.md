# Esercizi

## Funzioni e condizioni:

- Crea una funzione che prende in argomento un numero e ritorna True se è divisibile per 17, False se non lo è. Verifica che funzioni chiamandola per 15 e 34, printando il risultato. **Hint:** prova a usare l'operatore modulo "<code>%</code>"

## Liste

- Crea una lista di almeno 4 elementi e printala, poi crea una funzione che prende in argomento una lista e ne scambia il primo e l'ultimo elemento. Chiama la funzione e printane il risultato.
**Hint:** In una lista <code>l</code> puoi usare la notazione <code>l[-1]</code> per selezionare l'ultimo elemento di <code>l</code>

## Cicli

- (Valutazione p-adica) Crea una funzione che prende in argomento due numeri e trova il più grande esponente al quale il primo divide il secondo.
Controlla se funziona cercando la massima potenza di 3 che divide 324
**Procedimento:**
    - Definisci la funzione che prende in argomento p, n
    - inizializza una variabile k, l'esponente di p, inizialmente 0
    - inizia un ciclo che prosegue fintanto che n è divisibile per p^(k+1), durante il quale fa aumentare k di 1
    - ritorna k
    - chiama la funzione su 3, 324

## Fibonacci

- Crea una funzione che trova i primi n numeri della sequenza di fibonacci e testala sui primi 20. **Procedimento:**
    - Definisci una funzione che prende come argomento n, cioè quanti numeri di Fibonacci verranno calcolati
    - Inizializza una lista contente 0, 1
    - Avvia un ciclo for che itera la variabile i nei numeri da uno a n. Questo aggiungerà alla lista l'i-esimo numero di Fibonacci, dopo aver verificato che i sia maggiore di 1
    - ritorna la lista
    - chiama la funzione con parametro 20 per verificare che funzioni
