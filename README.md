# Endpoints propagation
Code for endpoints propagation of intervals. 

* The code is exponential in the number of interval inputs (2^n). So there is little point in vectorising the code. 
* Endpoints propagation is exact only for functions that are monotonic in the number of inputs. 

This propagation can be run independently from an interval arithemtic library. 

On a personal computer a 23 input intervals propagation takes about 129.02s with the Python 'sum' function (8388608 evaluations of the 'sum' in plain Python). The evaluation time increases exponentially with the number of inputs. In particular, the observed trend is that the run time nearly doubles for each additional input. 
