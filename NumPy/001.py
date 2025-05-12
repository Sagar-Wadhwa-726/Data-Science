# Lists are flexible but are slow since list elements are slow since they are stored in the form of pointers in non-contigious memory allocation 

# This makes a difference whne we are having a large data set (in millions)

# In this case we can use numerical python library - NumPy since these are faster than python lists, use less memory (wrote in C in the backedn which is fast). Supports vectorized operations (no explicit loops needed), and has build in mathematical functions

