def find_target(numbers, target):
    """Return the index of target in numbers, or -1 if not found."""
    for index, value in enumerate(numbers):
        if value == target:
            return index
    return -1


def count_evens(numbers):
    """Return the number of even values in numbers."""
    count = 0
    for value in numbers:
        if value % 2 == 0:
            count += 1
    return count


def list_summary(numbers):
    """Return (min_value, max_value, difference) for the list."""
    if not numbers:
        return None, None, None

    min_value = numbers[0]
    max_value = numbers[0]
    for value in numbers:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value

    return min_value, max_value, max_value - min_value


if __name__ == "__main__":
    sample = [3, 8, 1, 6]
    print("find_target:", find_target(sample, 6))
    print("count_evens:", count_evens(sample))
    print("list_summary:", list_summary(sample))
