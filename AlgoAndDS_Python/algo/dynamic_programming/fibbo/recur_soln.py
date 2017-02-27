def calc_fibbo(number):
    if number == 0 or number == 1:
        return number
    else:
        return calc_fibbo(number-1) + calc_fibbo(number - 2)
    
num = 0
while True:
    num = int(input("Enter Number (-1 to exit)"))
    if num == -1:
        break
    print("Fibbo of " + str(num) + ": " + str(calc_fibbo(num))) 