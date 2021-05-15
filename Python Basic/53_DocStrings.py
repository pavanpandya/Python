def test(a):
    '''
    Info: This Function test and prints the parameter a
    '''
    # The above comment is called Doc-String
    print(a)


test('Pavan Pandya')
test('Astha Pandya')
# when someone hover over the function test(), The Info of the function will get poped up. And this is because of Doc-String.

# We can also use help function to see what test function does.
help(test)

# We can also use doc dunder to see what test function does.
print(test.__doc__)
