def gen():
    for i in range(5):
        yield i

g = gen()

print("Manual next():")
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print("\nLoop:")
for x in gen():
    print(x)
