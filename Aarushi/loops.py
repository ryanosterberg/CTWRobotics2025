def fn_a(num):
    if num > 3:
        print("Fizz")

def fn_b(num):
    if num > 2 and num < 4:
        print("Fizz")
for i in range(6):
    fn_a(i)