# Scope - What variables do i have access to?

# Rules:
# 1. Start with Local Scope. (Inside it's Own Block)
# 2. Check the Parent Local Scope.
# 3. Check the Global Scope.
# 4. Built-in Python Function.

a = 1


def confusion():
    a = 5
    return a


def Parent():
    a = 10

    def child():
        return a
    return child()


def test():
    return sum


#my_answer = 5
print(confusion())
#my_answer = 1
print(a)

print(Parent())
print(test())
# Here first it(test Function) will check the variable 'sum' in its local scope,
# then will check its parent local scope, then will check the global scope and finally at the end will check the built-in Function scope.
