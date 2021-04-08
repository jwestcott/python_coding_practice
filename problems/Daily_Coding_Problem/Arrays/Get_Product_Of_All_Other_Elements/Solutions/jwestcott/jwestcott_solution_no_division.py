def product_of_all_other_elements(arr: list) -> list:
    result = len(arr) * [0]
    for i in range(len(arr)):
        sub_array = arr[0:i] + arr[(i + 1):]
        result[i] = find_product(sub_array)
    return result


def find_product(arr: list) -> int:
    product = 1
    for i in arr:
        product *= i
    return product


if __name__ == "__main__":
    input_array = [1, 2, 3, 4, 5]
    print("input: {}, output: {}".format(input_array, product_of_all_other_elements(input_array)))
