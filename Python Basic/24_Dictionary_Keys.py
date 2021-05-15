Dictionary = {
    123: [1, 2, 3],
    True: 2
    # [100]: True  # This will throw an error: unhashable type: 'list'
    # Here Where we use list as key it will throw an error as list are mutable.
}

# A Key needs to be immutuable(That can not be changed)
# A key has to be unique. and if there are two keys with same name then in the output the last value assigned to key will be printed

print(Dictionary)
