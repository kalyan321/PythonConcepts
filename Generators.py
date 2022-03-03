# Python3 program for demonstrating
# Generators Produces Data
# Coroutines Consume Data

# this function returns 1 to 100 numbers
def generator_example():
    for num in range(1, 101):
        yield num


def calling_generator():
    for val in generator_example():
        print(val)


# Coroutine Example
def print_name(prefix):
    print("Searching prefix:{}".format(prefix))
    while True:
        name = (yield)
        print(name)
        if prefix in name:
            print(name)


def call_corutine():
    # calling coroutine, nothing will happen
    corou = print_name("Dear")

    # This will start execution of coroutine and
    # Prints first line "Searching prefix..."
    # and advance execution to the first yield expression
    corou.__next__()

    # sending inputs
    corou.send("Atul")
    corou.send("Dear Atul")


if __name__ == "__main__":
    calling_generator()
    call_corutine()
