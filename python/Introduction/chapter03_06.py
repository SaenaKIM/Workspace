# Chapter03-6
# Sets
# Sets Type( unordered, duplication X)

# declaration
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = {'foo', 'bar', 'baz', 'foo', 'qux'}
f = {42, 'foo', (1, 2, 3), 3.14159}

print('a - ', type(a), a)
print('b - ', type(b), b)
print('c - ', type(c), c)
print('d - ', type(d), d)
print('e - ', type(e), e)
print('f - ', type(f), f)

# convert to tuple
t = tuple(b)
print('t - ', type(t), t)
print('t - ', t[0], t[1:3])


# convert to list
l = list(c)
l2 = list(e)
print('l - ', type(l), l)
print('l - ', l[0], l[1:3])
print('l2 - ', type(l2), l2)

# lenght
print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))

# usage of set
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print('s1 & s2 : l - ', s1 & s2)
print('s1 intersection s2 : l - ', s1.intersection(s2))

print('s1 | s2 : l - ', s1 | s2)
print('s1 union s2 : l - ', s1.union(s2))

print('s1 - s2 : l - ', s1 - s2)
print('s1 difference s2 : l - ', s1.difference(s2))

# has not duplicate element
print('is disjoint l - ', s1.isdisjoint(s2))

# subset
print('issubset : l - ', s1.issubset(s2))
print('issuperset : l - ', s1.issuperset(s2))


# add, remove, discard 
s1 = set([1, 2, 3, 4])
s1.add(5)
print('s1 - ', s1)

s1.remove(2)
print('s1 - ', s1)
# s1.remove(7)

s1.discard(3)
print('s1 - ', s1)

#s1.discard(7)

#This method is different from the remove() method, because the remove() method will raise an error if the specified item does not exist, and the discard() method will not.

# clear
s1.clear()