def mult(n, m): 
    if n == 0 or m == 0:
        return 0
    else:
        result = n + mult(n, abs(m) - 1)
        if m < 0:
            return -result
        else:   
            return result

print(mult(-7, -8))
assert mult(2,0) == 0
assert mult(2,2) == 4
assert mult(0,2) == 0
assert mult(-1,2) == -2
assert mult(1,-2) == -2
assert mult(-1,-2) == 2
