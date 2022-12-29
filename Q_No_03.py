t_1 = (1, 4, 9, 16, 25, 36)
print(t_1)
t_modified = tuple(x**2 for x in t_1)
print(t_modified)


element = t_modified[4]
print(element)

  
t_sliced = t_modified[1:4]
print(t_sliced)
