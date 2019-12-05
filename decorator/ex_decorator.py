def div_decorator(func):
    def inner(a, b):
        if b == 0:
            print "Division cannot be performed with denominator equal to zero"
            return
        return func(a, b)
    return inner


@div_decorator
def div(a, b):
    print a/ b

if __name__ == "__main__":
    div(10, 0)