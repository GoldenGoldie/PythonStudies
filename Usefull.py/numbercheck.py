def numbercheck(i):
    if i.isdigit():
        return int(i)
    else:
        return "no number"
    
x = "f"

y = "2"

x =numbercheck(x)
print(x)
y = numbercheck(y)
print(y)