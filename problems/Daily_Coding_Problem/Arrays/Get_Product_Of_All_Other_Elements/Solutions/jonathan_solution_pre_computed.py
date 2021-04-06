def assert_equals(expected: object, received: object):
    success_character = "\u2717"
    if expected == received:
        success_character = "\u2713"
    print("Expected: {}, Received: {} {}".format(expected, received, success_character))


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
    assert_equals([120, 60, 40, 30, 24], product_of_all_other_elements([1, 2, 3, 4, 5]))
    assert_equals([2, 3, 6], product_of_all_other_elements([3, 2, 1]))
