# Set Operation Summary Table
| Operation                | Symbol/Method                  | Result                   | Example Use Case      |                      |
| ------------------------ | ------------------------------ | ------------------------ | --------------------- | -------------------- |
| **Union**                | \`                             | `, `.union()\`           | All unique items      | Merge customer lists |
| **Intersection**         | `&`, `.intersection()`         | Common items             | People in both groups |                      |
| **Difference**           | `-`, `.difference()`           | In one but not the other | Students absent       |                      |
| **Symmetric Difference** | `^`, `.symmetric_difference()` | In either but not both   | Exclusive memberships |                      |
| **Subset**               | `.issubset()`                  | True/False               | Curriculum check      |                      |
| **Superset**             | `.issuperset()`                | True/False               | Permission check      |                      |
| **Disjoint**             | `.isdisjoint()`                | True/False               | No overlap            |                      |

# Python's Collection types
There are four collection data types in the Python programming language:
- `List` is a collection which is ordered and changeable. Allows duplicate members.
- `Tuple` is a collection which is ordered and unchangeable. Allows duplicate members.
- `Set` is a collection which is unordered, unchangeable`r1`, and unindexed. No duplicate members.
- `Dictionary` is a collection which is ordered`r2` and changeable. No duplicate members.

---
- *`Ref 1`Set items are unchangeable, but you can remove and/or add items whenever you like.
- *`Ref 2`As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.

# Functions
## Parameters or Arguments?
The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:
- A parameter is the variable listed inside the parentheses in the function definition.
- An argument is the value that is sent to the function when it is called.

## Arbitrary Arguments, *args
If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly

## Arbitrary Keyword Arguments, **kwargs
If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly

## Positional-Only Arguments
You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
To specify that a function can have only positional arguments, add `,` `/` after the arguments:
```python
 def my_function(x):
    print(x)

 my_function(4)
```
Without the `,` `/` you are actually allowed to use keyword arguments even if the function expects positional arguments.

But when adding the `,` `/` you will get an error if you try to send a keyword argument.

## Keyword-Only Arguments
To specify that a function can have only keyword arguments, add *, before the arguments:
```python
def my_function(*, x):
  print(x)

my_function(x = 3)
```
Without the `*` `,` you are allowed to use positional arguments even if the function expects keyword arguments.

But with the `*` `,` you will get an error if you try to send a positional argument: