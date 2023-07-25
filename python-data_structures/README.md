# Python - Data Structures: Lists, Tuples

This repository provides examples and explanations of two important data structures in Python: Lists and Tuples.

## Lists

Lists in Python are versatile and commonly used data structures that allow you to store collections of items. Each item in a list is indexed, starting from 0, which means you can access elements using their index. Lists are mutable, meaning you can modify their content after creation. You can add, remove, and update elements in a list.

### Basic Operations with Lists

- Creating a list: Lists are created using square brackets. For example: `my_list = [1, 2, 3, 4]`.

- Accessing elements: You can access elements in a list using their index. For example: `first_element = my_list[0]`.

- Modifying elements: Lists allow you to modify their elements by assigning new values to specific indices. For example: `my_list[1] = 10`.

- Adding elements: You can add elements to the end of a list using the `append()` method. For example: `my_list.append(5)`.

- Removing elements: You can remove elements from a list using the `remove()` method or the `del` statement. For example: `my_list.remove(3)` or `del my_list[1]`.

## Tuples

Tuples are similar to lists, but they are immutable, meaning their elements cannot be changed after creation. Tuples are created using parentheses, and like lists, they can store multiple elements of different data types.

### Basic Operations with Tuples

- Creating a tuple: Tuples are created using parentheses. For example: `my_tuple = (1, 'hello', 3.14)`.

- Accessing elements: Elements in a tuple are accessed using their index, just like lists. For example: `first_element = my_tuple[0]`.

- Tuple unpacking: You can unpack a tuple into multiple variables in a single assignment. For example: `a, b, c = my_tuple`.

- Combining tuples: Tuples can be combined using the `+` operator. For example: `combined_tuple = my_tuple + (4, 5)`.

- Tuple methods: Tuples have limited methods compared to lists since they are immutable. However, you can use methods like `count()` and `index()`.

In this repository, you will find practical examples and code snippets to help you understand these data structures better. Feel free to explore the provided Python files to grasp the concepts and use cases of Lists and Tuples.

Happy coding!