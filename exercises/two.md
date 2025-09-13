# 🐍 Python List Practice Questions

This repository contains a set of **Python List questions** to test your knowledge.
The questions progress from **basic** to **intermediate**, and finally include **3 tough challenges**.

---

## 🔹 Basic Questions

1. How do you create a list in Python? Give two different examples.
2. What will be the output of this code?

   ```python
   my_list = ["apple", "banana", "cherry"]
   print(my_list[1])
   ```
3. How do you find the length of a list?

---

## 🔹 Intermediate Questions

4. Write Python code to add `"orange"` to this list:

   ```python
   fruits = ["apple", "banana", "cherry"]
   ```
5. What is the difference between `append()` and `extend()` in lists?
6. Suppose you have:

   ```python
   numbers = [10, 20, 30, 40, 50]
   ```

   How can you change `30` to `35`?
7. Write Python code to remove `"banana"` from this list:

   ```python
   fruits = ["apple", "banana", "cherry", "banana"]
   ```

   *(Hint: Think about `remove()` vs `pop()` vs `del`)*
8. Given this list:

   ```python
   nums = [5, 2, 9, 1, 7]
   ```

   * Sort it in **ascending order**.
   * Sort it in **descending order**.
9. You have a list:

   ```python
   colors = ["red", "green", "blue"]
   ```

   How can you insert `"yellow"` at position `1`?
10. Challenge: Write code that checks if `"apple"` is in this list:

    ```python
    basket = ["mango", "apple", "grape"]
    ```

---

## 🔹 Tough Questions

11. **Nested Lists**
    What will be the output of the following code? Explain why:

    ```python
    data = [[1, 2], [3, 4], [5, 6]]
    print(data[1][0] + data[-1][-1])
    ```

12. **List Comprehension with Condition**
    Write one line of Python code that creates a list of all **squares of even numbers** between 1 and 10 (inclusive).
    👉 Example output:

    ```python
    [4, 16, 36, 64, 100]
    ```

13. **Removing Duplicates While Preserving Order**
    You have the list:

    ```python
    items = ["apple", "banana", "apple", "orange", "banana", "grape"]
    ```

    Write Python code that removes duplicates **but keeps the original order**, so the result is:

    ```python
    ["apple", "banana", "orange", "grape"]
    ```

---

### 🧩 Hard Question 1 – Filter & Transform

You have a list of numbers:

```python
nums = [3, 8, -2, 5, -7, 10, 0, -1]
```

Write Python code that creates a **new list** containing only the **positive numbers**, but each number should be multiplied by `2`.

👉 Expected output:

```python
[6, 16, 10, 20]
```

---

### 🧩 Hard Question 2 – Find Most Frequent Element

You have a list:

```python
letters = ["a", "b", "a", "c", "b", "a", "d", "b"]
```

Write Python code that finds the element that appears the most times in the list and prints:

```
The most frequent element is: a
```

(since `"a"` appears 3 times, which is more than any other).

---