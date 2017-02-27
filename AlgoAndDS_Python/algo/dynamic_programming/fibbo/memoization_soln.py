def calc_fibbo(number, arr):
    if number == 0 or number == 1:
        return number
    elif arr[number] == 0:
        arr[number] = calc_fibbo(number-1, arr) + calc_fibbo(number - 2, arr)
    return arr[number]
    
num = 0

while True:
    num = int(input("Enter Number (-1 to exit)"))
    if num == -1:
        break
    arr = [0 for _ in range(num+1)]
    print("Fibbo of " + str(num) + ": " + str(calc_fibbo(num, arr))) 
    print(arr)