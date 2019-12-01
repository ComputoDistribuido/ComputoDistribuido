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


def printCode(message):
    os.system("clear")
    print("Ejecucion de " + message)
    print()


def printMenuWait():
    print()
    print("Presione enter para regresar al menu")
    sys.stdin.readline()
    printMenu()


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


main()
