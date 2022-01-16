#
#

def greetings(fn):
    def wrapper(name):
        import time
        start = time.time()

        print("Hello!")
        fn(name)
        print("Good bye!")

        time.sleep(1)  # sleep 1 second

        stop = time.time() - start

        print(stop)
        # return stop

    return wrapper


@greetings
def goodmorning(name):
    print(f"My name is {name}")


@greetings
def goodday(name):
    print(f"My name is {name}")


goodmorning("Arif")
# Hello!
# My name is Arif
# Good bye!

goodday("Ali")
# Hello!
# My name is Ali
# Good bye!
