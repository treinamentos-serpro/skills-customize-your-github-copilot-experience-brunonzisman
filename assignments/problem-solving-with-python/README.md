# 📘 Assignment: Problem Solving with Python

## 🎯 Objective

Practice algorithmic thinking and list processing by solving simple search, counting, and analysis problems using Python loops and conditionals.

## 📝 Tasks

### 🛠️ Linear Search

#### Description
Write a function called `find_target(numbers, target)` that searches a list for a value and returns its location.

#### Requirements
Completed program should:

- Take a list of integers named `numbers` and an integer `target`.
- Return the index of the first occurrence of `target` in the list.
- Return `-1` if the target is not found.
- Example usage:
  ```python
  print(find_target([3, 7, 2, 7], 7))  # 1
  print(find_target([1, 2, 3], 4))    # -1
  ```

### 🛠️ Count Even Numbers

#### Description
Write a function called `count_evens(numbers)` that counts how many even values are in a list.

#### Requirements
Completed program should:

- Take a list of integers named `numbers`.
- Use a loop and conditional checks to count even numbers.
- Return the total count of even integers.
- Example usage:
  ```python
  print(count_evens([1, 2, 3, 4, 5, 6]))  # 3
  ```

### 🛠️ List Analysis Challenge

#### Description
Write a function called `list_summary(numbers)` that analyzes a list of integers and returns key values.

#### Requirements
Completed program should:

- Return a tuple containing the smallest number, the largest number, and the difference between them.
- Return `(None, None, None)` if the list is empty.
- Example usage:
  ```python
  print(list_summary([5, 3, 10]))  # (3, 10, 7)
  print(list_summary([]))          # (None, None, None)
  ```
