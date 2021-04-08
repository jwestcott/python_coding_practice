def product_of_all_other_elements(arr: list) -> list:
    prefix_array = get_prefix_array(arr)
    postfix_array = get_postfix_array(arr)
    return [pre * post for pre, post in zip(prefix_array, postfix_array)]


def get_prefix_array(arr: list) -> list:
    prefix_array = [1]
    for i in range(1, len(arr)):
        prefix_array.append(prefix_array[i - 1] * arr[i - 1])
    return prefix_array


def get_postfix_array(arr: list) -> list:
    arr_copy = arr.copy()
    arr_copy.reverse()
    postfix_array = get_prefix_array(arr_copy)
    postfix_array.reverse()
    return postfix_array


if __name__ == "__main__":
    input_array = [1, 2, 3, 4, 5]
    print("input: {}, output: {}".format(input_array, product_of_all_other_elements(input_array)))
