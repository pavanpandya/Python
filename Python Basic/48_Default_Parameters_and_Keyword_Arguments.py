def say_hello(name, emoji):
    print(f'Hello {name} Good Morning {emoji}')


# Keyword Arguments - We tell the interpreter Explicitlity that name equals to this and emoji equals to this.
# Bad Practice as it makes the code more complicated.
say_hello(name='astha', emoji='<3')


# Default Parameters - If no argument is given to a particular keyword then default is taken at that time.
def say_hello2(name='Pavan Pandya', emoji='*'):
    print(f'Hello {name} Good Morning {emoji}')


# Here Default paramter will get printed
say_hello2()
