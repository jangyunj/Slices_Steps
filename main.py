mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]


a = mylist[1:5]  # Slicing- last index is excluded
print(a)

b = mylist[:5]  # Starts from beginning
print(b)

c = mylist[1:]  # Goes to the end
print(c)

d = mylist[::1]  # Beginning, End, Step
print(d)

e = mylist[::2]  # From beginning to end by 2 steps
print(e)

f = mylist[::-1]  # End to beginning -- Reverses the list
print(f)

g = mylist[::-2]  # Reverses by 2 steps
print(g)
