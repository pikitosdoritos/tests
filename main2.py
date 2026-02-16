def log(func):
    def wrapper():
        print("=== start ===")
        func()
        print("=== end ===")
    return wrapper


@log
def say_hello():
    print("Hello from function!")


@log
def say_bye():
    print("Bye from function!")


say_hello()
print()
say_bye()
