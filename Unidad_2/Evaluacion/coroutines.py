def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    try:
        while True:
            # yeild used to create coroutine
            name = (yield)
            if prefix in name:
                print(name)
    except GeneratorExit:
        print("Closing coroutine!!")


def start():
    corou = print_name("Dear")
    corou.__next__()
    corou.send("James")
    corou.send("Dear James")
    corou.close()
