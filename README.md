# WILT

Banele's what I learned today

## Python
---

#### For loops or Next - 27/03/18

To grab the first element in an array that satisfies a particular predicate, one can either use a for loop or make use of the `next` function.

Concretely:
```
for i in range(100):
    if i == 9:
      break;
```

does the same thing as:
```
  next((x for x in range(100) if x == 9), None)
```

But in terms of performance, the loops are better off, yet to investigate why. Evidence in #1.
