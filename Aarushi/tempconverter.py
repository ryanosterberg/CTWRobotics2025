def ctof(c):
    return (1.8 * c) + 32
def ftoc(f):
    return (f-32)/1.8

# Now change 0C to F:
print(ctof(0))

# Change 100C to F:
print(round(ctof(100), 2))

# Change 40F to C:
print(round(ftoc(40),2))

# Change 80F to C:
print(ftoc(80))