print(len('Hellooo'))

quote = 'To be or not to be'

print(quote.upper())
print(quote.capitalize())
print(quote.lower())
print(quote.find('be'))
# Here Changes will not reflect in the actual string as "strings are immutable".
print(quote.replace('be', 'me'))

# This will create new string but will not replace the actual string
quote2 = print(quote.replace('be', 'me'))

print(quote)
