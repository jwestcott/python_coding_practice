def assert_equals(expected: object, received: object):
    success_character = "\u2717"
    if expected == received:
        success_character = "\u2713"
    print("Expected: {}, Received: {} {}".format(expected, received, success_character))


def product_of_all_other_elements(arr: list) -> list:
    pass


if __name__ == "__main__":
    assert_equals([120, 60, 40, 30, 24], product_of_all_other_elements([1, 2, 3, 4, 5]))
    assert_equals([2, 3, 6], product_of_all_other_elements([3, 2, 1]))
