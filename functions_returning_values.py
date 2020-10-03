def add(x, y):
    print(x + y)

add(5, 8) # 13
result = add(5, 8)
print(result) # None. This means after running, line 5 did something that made result = none.
#Functions return None by default.

#If we do this instead:
def add(x, y):
    return(x + y) # Return terminates the function when the line is run and gives the value returned back to the caller.

result = add(5, 8)
print(result) # 13

def divide(dividend, divisor):
    if divisor != 0:
        return (dividend/divisor)
    else:
        return ("You fool, you can't do that!")

result = divide(18, 6)
print(result)

result = divide(18, 0)
print(result)

#It's better for a function to have the same return data type within itself, because:
def divide(dividend, divisor):
    if divisor != 0:
        return (dividend/divisor)
    else:
        return ("You fool!")

#if we do the below,
result = divide(18, 0) * 5
print(result) # You fool!You fool!You fool!You fool!You fool!
#But if we do this:
result = divide(18, 5) * 3 # 10.8
print(result)
# So keep the return data type the same.