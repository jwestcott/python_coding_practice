def product_of_all_other_elements(arr: list) -> list:
    product = find_product(arr)
    result = len(arr) * [product]
    for i in range(len(arr)):
        result[i] //= arr[i]
    return result


def find_product(arr: list) -> int:
    product = 1
    for i in arr:
        product *= i
    return product


if __name__ == "__main__":
    input_array = [1, 2, 3, 4, 5]
    print("input: {}, output: {}".format(input_array, product_of_all_other_elements(input_array)))
