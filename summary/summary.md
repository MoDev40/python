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