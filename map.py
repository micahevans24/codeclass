#map.py

def map(func, l):
    """ Accepts a function (func) and a list (l).
        Returns a new list that is the result of applying func
        to every element of l.
    """
	if l == []:
		return []

	else:
		newInteger = l[0] + 6
		int_plus_six = map(func, l[1:])
		return [newInteger] + int_plus_six

print(list(map(lambda x: x + 6, [6, 8, 19, 22])))

assert map(lambda x: x * 2, [1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10]
assert map(len, ['hello', 'bob']) == [5, 3]
