def binarySearch(array, key):
    index = None
    lower = 0
    upper = len(array)- 1
    while lower <=upper:
        mid = int((lower+upper)/2)
        if key == array[mid]:
            index = mid
            break
        elif key < array[mid]:
            upper = mid-1 
        elif key > array[mid]:
            lower = mid + 1 
    return index

if __name__ == '__main__':
    n = int(input("Enter the number of array: "))
    arr  = list(map(int, input("Enter the elements with space: ").split()))[:n]
    arr = sorted(arr)
    print(arr)
    while True:
        k = int(input("Enter the searching value from the list: "))
        result = binarySearch(arr, k)
        if result == None:
            print(f"The searching value is not in the list. Please Search again.")
        else:
            print(f"The searching value index is {result+1}")

