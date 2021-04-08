#given an arry of integers, return a new array such that each element at
#index i of the new array is the product of all the numbers in the original
#array except the one at i

#if [1, 2, 3, 4, 5] then [120, 60, 40, 30, 24]
#if [3, 2, 1] then [2, 3, 6]

#extra credit: do it without division


arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 20, 1]

def product_elements(arr):
    new_array = []
    product = 1
    result = 1
    for i in arr:
        product *= i

    for i in arr:
        result = product / i
        new_array.append(result)
    return new_array

print(product_elements(arr1))
print(product_elements(arr2))

def product_elements_v2(arr):
    new_array = []
    product = 1
    for i in range(len(arr)):
        for j in arr:
            if j != arr[i]:
                product *= j
        new_array.append(product)
        product = 1
    return new_array

print(product_elements_v2(arr1))
print(product_elements_v2(arr2))
