def linear_search(arr, num):
    for i in arr:
        if i == num:
            print(arr.index(i))

arr = [34,67,423,234,646,23,6,4,3,2,1]
linear_search(arr,2)

