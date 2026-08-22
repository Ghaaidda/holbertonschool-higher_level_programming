# Immutable and Mutable Types in Python

One of the most important things I learned about Python is the difference between **mutable** and **immutable** objects. It also helps explain why variables sometimes appear to point to the same object, why an object's address can change, and what Python is doing behind the scenes to save memory.

## Variables Don't Actually Store Values

In Python, a variable is better thought of as a **name that refers to an object** rather than a box that directly contains a value.

For example:

```python
x = 10
```

Here, `x` refers to an integer object containing `10`.

You can see the object's memory identity using `id()`:

```python
x = 10
print(id(x))
```

If we create another variable:

```python
y = 10

print(id(x))
print(id(y))
```

You will notice that both variables have the **same address**.

This doesn't mean that Python always creates a new object for every variable.

## Python Interning

Python sometimes reuses objects instead of creating new ones. This is called **interning**.

The idea is simple: if Python already has an object representing a value that can safely be reused, it can make multiple variables refer to that same object. This saves memory and can make some operations more efficient.

For example:

```python
a = 10
b = 10

print(a is b)
```

This will typically print:

```text
True
```

Both variables refer to the same integer object.

However, you should **not rely on interning** when comparing values. Use `==` to compare values and `is` to check whether two variables refer to the exact same object.

```python
a == b   # Compare values
a is b   # Compare object identity
```

## Immutable Types

An **immutable object cannot be changed after it has been created**.

Common immutable types include:

* `int`
* `float`
* `bool`
* `str`
* `tuple`

Consider an integer:

```python
x = 10
old_address = id(x)

x = 20

print(id(x))
```

It might look like we changed `10` into `20`, but we actually didn't change the integer object.

Instead, Python makes `x` refer to another integer object:

```text
x → 10
```

becomes:

```text
x → 20
```

The original `10` object itself remains unchanged.

### The Address Changes

This is an important consequence of immutability:

> When you "change" the value of an immutable object, you are actually making the variable refer to a different object.

For example:

```python
x = 10
print(id(x))

x = 20
print(id(x))
```

The identity of `x` can change because `x` is now referring to a different integer object.

So when talking about immutable objects, it's more accurate to say:

```python
x = 10
x = 20
```

means:

> "Make `x` stop referring to the `10` object and refer to the `20` object."

Not:

> "Change the `10` object into a `20` object."

## Mutable Types

A **mutable object can be changed after it has been created**.

A common example is a list:

```python
numbers = [1, 2, 3]

old_address = id(numbers)

numbers.append(4)

print(numbers)
print(id(numbers))
```

The list itself was modified:

```text
[1, 2, 3]
      ↓
[1, 2, 3, 4]
```

The object remains the same object, so its identity generally stays the same.

This is different from what happens with an immutable object such as an integer.

## Tuple Syntax Can Be Confusing

One small Python detail that is easy to miss is that **the comma creates a tuple, not the parentheses**.

This:

```python
(1)
```

is simply an integer:

```python
type((1))
# <class 'int'>
```

But this:

```python
(1,)
```

is a tuple:

```python
type((1,))
# <class 'tuple'>
```

And:

```python
()
```

is an empty tuple.

So:

```python
(1)      # int
(1,)     # tuple
()       # tuple
```

The comma is what matters when creating a one-element tuple.

## Conclusion

This is why understanding **variables, references, object identity, mutability, and interning** together gives you a much clearer picture of how Python handles values in memory.
