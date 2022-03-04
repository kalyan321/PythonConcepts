from functools import lru_cache
# A function is called first class objects if :
#     1] A function is an instance of Object
#     2] Function can be assigned to a Variable
#     3] Pass the function as a parameter to another function
#     4] return the function from a function
#     5] you can store them in data structures like lists, hashtable ...

@lru_cache()

# Functions as Objects
def power(num, x):
    return num ** x


# Passing function as argument
def multiply_by_two(num):
    return num * 2


def randomnumber(num, func):
    ans = int(func(num * 0.8))
    return ans


# returning function from another function
def create_adder(x):
    def adder(y):
        return x + y
    return adder


if __name__ == "__main__":
    # pow = power
    # print(pow(2, 3))  # output is 8

    # rand = randomnumber
    # ans = rand(3, multiply_by_two)
    # print(ans)
    add = create_adder(3)
    print(add(2))
