def calc_fibbo(number):
    arr = [0] * (number+1)
    arr[0] = 0
    arr[1] = 1
    for cntr in range(2, number+1):
        arr[cntr] = arr[cntr-1] + arr[cntr-2]
    return arr[len(arr)-1]
    
num = 0

while True:
    num = int(input("Enter Number (-1 to exit)"))
    if num == -1:
        break
    print("Fibbo of " + str(num) + ": " + str(calc_fibbo(num))) 
