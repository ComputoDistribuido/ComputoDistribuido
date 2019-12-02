import processes
import courutines
def promptMenu():
    print('======= Seleccione el numero de practica: ...')
    print('1. Multi procesos')

while True:
    promptMenu()
    testIndex = input()
    if testIndex == '1':
        processes.print_func(continent='Asia')
        print('unooo')
    if testIndex == '2':
        corou = courutines.print_name("Dear")
        corou.__next__()
        corou.send("James")
        corou.send("Dear James")
        corou.close()
    else:
        print('===== Exit =====')
        break
