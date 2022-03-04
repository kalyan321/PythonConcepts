# Python3 program for demonstrating Generators

# If a function contains yield keyword, then that function is known as Generator functions
# Genarators functions returns generators objects
# Generator Objects are used either by calling the next method on the generator object or
# using generator object in "for in " loop
# Generators Produces Data

# this function traverse 1 to 100 numbers
def generator_example():
    for num in range(1, 101):
        yield num


# this function prints 1 to 100 numbers
def generator_object_using_forin_loop():
    for val in generator_example():
        print(val)


# this function prints 1, 2 because we used only two times the next
def generator_object_using_next():
    generator = generator_example()
    print(generator.__next__())
    print(next(generator))


if __name__ == "__main__":
    generator_object_using_next()
    # generator_object_using_forin_loop()
