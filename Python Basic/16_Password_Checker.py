username = input('Enter Your Username: ')
password = input('Enter Your Password: ')

password_lenth = len(password)
hidden_password = '*' * password_lenth

print(
    f'Hello, {username}, Your Password {hidden_password} is {password_lenth} letters long')
