## Examen

To start we need to import the following packages that contain the functions and modules to create the program.
```python
import asyncq
import countasync
import processes
import os
import sys
import threads
import coroutines
import countsync
import rand
import chained
import areq
import poolApply
import poolMap
import poolStarmap
```

We create a function that prints a menu with selection options to navigate in the program
```python
def printMenu():
    os.system("clear")
    print("-------------MENU--------------")
    print()
    print(" Programacion Asincrona")
    print()
    print("   1. CountAsync")
    print("   2. CountSync")
    print("   3. Random")
    print("   4. Chained Coroutines")
    print("   5. Async Queue")
    print("   6. Asynchronous Request")
    print()
    print(" Procesamiento Paralelo")
    print()
    print("   7. Multiple Processes")
    print("   8. Multiple Threads")
    print("   9. Coroutines")
    print("   10. Pool.apply")
    print("   11. Pool.map")
    print("   12. Pool.starmap")
    print()
    print("0. Salir")
    print()
```
This function is used as printing personalized messages when programs are running
```python
def printCode(message):
    os.system("clear")
    print("Ejecucion de " + message)
    print()
```

This function is used to add a message back to the main menu within the running program
```python
def printMenuWait():
    print()
    print("Presione enter para regresar al menu")
    sys.stdin.readline()
    printMenu()
```

The main function called main is the one that is responsible for directing the options with the programs and when selected, executes them.
```python
def main():
    printMenu()
    while 1 == 1:
        option = input("Seleccione el numero: ")

        if option == '7':
            printCode("Multiple Processes")
            processes.start()
            printMenuWait()
        elif option == '8':
            printCode("Multiple Threads")
            threads.start()
            printMenuWait()
        elif option == '9':
            printCode("Coroutines")
            coroutines.start()
            printMenuWait()
        elif option == '1':
            printCode("CountAsync")
            countasync.start()
            printMenuWait()
        elif option == '2':
            printCode("CountSync")
            countsync.start()
            printMenuWait()
        elif option == '3':
            printCode("Random")
            rand.start()
            printMenuWait()
        elif option == '4':
            printCode("Chained Coroutines")
            chained.start()
            printMenuWait()
        elif option == '5':
            printCode("Async Queue")
            asyncq.start()
            printMenuWait()
        elif option == '6':
            printCode("Asynchronous Request")
            areq.start()
            printMenuWait()
        elif option == '10':
            printCode("Pool.apply")
            poolApply.start()
            printMenuWait()
        elif option == '11':
            printCode("Pool.map")
            poolMap.start()
            printMenuWait()
        elif option == '12':
            printCode("Pool.starmap")
            poolStarmap.start()
            printMenuWait()
        elif option == '0':
            break
        else:
            print("Eliga una opcion valida [0-13]")
```

To start the program when it is invoked in the terminal we have to declare a call to the main () function.
```python
main()
```