def special_for(iterable):
    iterable = iter(iterable)
    while True:
        try:
            print(iterable)
            print(next(iterable))
        except StopIteration:
            break


special_for([1, 2, 3])
#  We loop through some iterable objects using next and you see that this object exists in same location.

# Output:

# <list_iterator object at 0x0151E7F0>
# 1
# <list_iterator object at 0x0151E7F0>
# 2
# <list_iterator object at 0x0151E7F0>
# 3
# <list_iterator object at 0x0151E7F0>


# How range works?
class My_gen():
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.current = self.first

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.last:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


gen = My_gen(50, 100)

for i in gen:
    print(i)
