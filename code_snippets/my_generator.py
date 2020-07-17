# using yield doesn't return values
# this function will rather hold the state


def first_n(n):
    for i in range(n):
        yield i


my_gen = first_n(5)
print(type(my_gen))

print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
# at this point the generator is exhausted
# there are no more values to generate on the fly
print(next(my_gen))

