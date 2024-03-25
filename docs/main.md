# Extract stack

## Motivation

more performant

documentation

vector relation to before and after functions, classes

## How

1. Get all stack trace
    
    ```python
    import traceback
    
    def f():
        g()
    
    def g():
        for line in traceback.format_stack():
            print(line.strip())
    
    f()
    ```
    
2. Save variable values

```jsx
import pickle

def sum():
    return 1+2

a = 3; b = [11,223,435];
g = sum
pickle.dump([a,b, g], open("trial.p", "wb"))

c,d, g = pickle.load(open("trial.p","rb"))

print(c,d, g) ## To verify

# use g
print(g()) # prints 10 bytes from the file
```