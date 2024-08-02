# Endpoints propagation
Code for endpoints propagation of intervals. 

* The code is exponential in the number of interval inputs (2^n). So there is little point in vectorising the code. 
* Endpoints propagation is exact only for functions that are monotonic in the number of inputs. 

This propagation can be run independently from an interval arithemtic library. 

On a personal computer a 23 input intervals propagation takes about 129.02s with the Python 'sum' function (8388608 evaluations of the 'sum' in plain Python). The evaluation time increases exponentially with the number of inputs. In particular, the observed trend is that the run time nearly doubles for each additional input. 

```python
    # 12 -> 0.68s   (2**12 = 4096)
    # 15 -> 0.92s   (2**15 = 32768)
    # 17 -> 2.11s   (2**17 = 131072)
    # 18 -> 3.77s   (2**18 = 262144)
    # 19 -> 7.39s   (2**19 = 524288)
    # 20 -> 14.74s  (2**20 = 1048576)
    # 21 -> 30.37s  (2**21 = 2097152)
    # 22 -> 62.19s  (2**22 = 4194304)
    # 23 -> 129.02s (2**23 = 8388608)
    # 24 -> 265.40s (2**24 = 16777216)
```

# Example 

```python
import numpy as np
from endpoints_propagation import a, endpoints_propagation_2n

X = a(19*[[1,2]])

print(X.shape)

def linearfun(*x): return -sum(x)

if __name__ == '__main__':

    print(endpoints_propagation_2n(X,linearfun))

    # (19, 2)
    # (-38.0, -19.0, (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))


```
