# 🚀 Day 5 - Functions & Exception Handling

## 📌 Topics Covered

### ✅ Functions
- Function Definition
- Function Call
- Parameters and Arguments
- return Statement
- print() vs return()
- Local Variables
- Global Variables
- Multiple Return Values

---

### ✅ Lambda Functions

Anonymous functions used for short operations.

Example:

```python
square = lambda x: x ** 2
```

---

### ✅ map()

Applies a function to every element in an iterable.

Example:

```python
numbers = [1,2,3]

list(map(lambda x:x*2,numbers))
```

Output

```
[2,4,6]
```

---

### ✅ filter()

Filters elements based on a condition.

Example

```python
list(filter(lambda x:x%2==0,numbers))
```

Output

```
[2]
```

---

### ✅ reduce()

Reduces an iterable into a single value.

```python
from functools import reduce

reduce(lambda a,b:a+b,[1,2,3,4])
```

Output

```
10
```

---

### ✅ Exception Handling

Used to prevent program crashes when runtime errors occur.

Keywords learned:

- try
- except
- else
- finally

Common Exceptions

- ZeroDivisionError
- ValueError
- IndexError
- TypeError
- FileNotFoundError

---

# 📚 Interview Questions Covered

- Difference between print() and return()
- Parameters vs Arguments
- Local vs Global Variables
- What are Lambda Functions?
- Difference between map(), filter(), and reduce()
- What is Exception Handling?
- Difference between ValueError and IndexError

---

# 💡 Key Takeaways

✔ Functions improve code reusability.

✔ Lambda functions provide concise one-line functions.

✔ map() transforms every element.

✔ filter() selects elements based on a condition.

✔ reduce() combines all elements into a single result.

✔ Exception handling makes programs more robust and user-friendly.

---

## 🚀 Progress

- ✅ Day 1
- ✅ Day 2
- ✅ Day 3
- ✅ Day 4
- ✅ **Day 5 Completed**
