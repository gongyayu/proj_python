import numpy as np
from py_mod import line_print, st_print, code_print, st_code, st_markline

### StartofFunc###

def py_np():
    # we can pass a list, tuple and any array-like object into array()
    #
    np_list = np.array(["numbers", 3, 6, 9, 12])
    np_tuple = np.array((3, 6, 9, 12))
    code_print(f"type: {type(np_list)}, np_array: {np_list}, np_array.dtype: {np_list.dtype} \
               \ntype: {type(np_tuple)}, a: {np_tuple}, a.dtype: {np_tuple.dtype}")
    #
    # dimensions
    #
    zero_d_arr = np.array(45)
    d_arr = np.array([1,2,4])
    dd_arr = np.array([[1,2,3],[4,5,6]])
    ddd_arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

    ds_arr = np.array([1,2,3,4], ndmin=5)                            # 5 diemnsions
    code_print(f"ds_arr: {ds_arr}, ds_arr.ndim: {ds_arr.ndim}")
    st_code(code_print(f''))
### EndofCodeSection###

def py_np_types():
    #
    # data types
    #  
    d_arr = np.array([1,2,4])        
    code_print(f"{'-' * 50}")
    code_print(f"d_arr: {d_arr}, d_arr.dtype: {d_arr.dtype}")
    c = np.array([[1, 2], [3, 4]], dtype=np.float64)
    code_print(f"type: {type(c)}, c: {c}, c.dtype: {c.dtype}")
    #
    # type conversion
    #
    arr = np.array([1.1, 2.1, 3.1])
    code_print(f"arr: {arr}, arr.dtype: {arr.dtype}")
    newarr = arr.astype('i')                                           # int32.  (int)-> int64
    code_print(f"newarr: {newarr}, newarr.dtype: {newarr.dtype}")
    boolarr = arr.astype(bool)
    code_print(f"boolarr: {boolarr}, boolarr.dtype: {boolarr.dtype}")

    st_code(code_print(f''))
### EndofCodeSection###

def py_np_attr():
    b = np.array([[1, 2], [3, 4]])
    code_print(f"dir(b): {dir(b)}")
    code_print(f"type: {type(b)}, b: {b}, b.shape: {b.shape}, b.ndim: {b.ndim}, b.size: {b.size}")
    st_code(code_print(f''))
### EndofCodeSection###

def py_np_indexing():
    arr_a = np.array([1,2,3])
    code_print(f"arr[0]: {arr_a[0]}")

    arr_b = np.array([[1,2,3,4,5], [6,7,8,9,10]])
    code_print(f"arr_b[0][1]: {arr_b[0][1]}")

    arr_c = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
    code_print(f"arr_c[0][1][2]: {arr_c[0][1][2]}")

    arr_d = np.array([[1,2,3,4,5], [6,7,8,9,10]])
    code_print(f"arr_d[1][-1]: {arr_d[1][-1]}")
    st_code(code_print(f''))
### EndofCodeSection###
    
def py_np_slicing():    
    arr_d = np.array([1, 2, 3, 4, 5, 6, 7])
    code_print(f"arr_d][1:5]: {arr_d[1:5]}, arr_d[4:]: {arr_d[4:]}, arr_d[:4]: {arr_d[:4]}")
    code_print(f"arr_d][-3:-1]: {arr_d[-3:-1]}, arr_d[1:5:2]: {arr_d[1:5:2]}, arr_d[::2]: {arr_d[::2]}")
    code_print(f"{'-' * 40}")
    arr_dd = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    code_print(f"arr_dd][1,1:4]: {arr_dd[1,1:4]}, arr_dd[0:2,2]: {arr_dd[0:2,2]}, arr_dd[0:2,1:4]: {arr_dd[0:2, 1:4]}")

    st_code(code_print(f''))
### EndofCodeSection###

def py_np_ops():
    d = np.zeros((2, 3))
    code_print(f"type: {type(d)}, d: {d}")
    
    e = np.ones((2, 3))
    code_print(f"type: {type(e)}, e: {e}")
    
    f = np.arange(0, 10, 2)
    code_print(f"type: {type(f)}, f: {f}")
    
    g = np.linspace(0, 1, 5)
    code_print(f"type: {type(g)}, g: {g}")
    
    h = np.random.rand(2, 3)
    code_print(f"type: {type(h)}, h: {h}")
    
    i = np.random.randint(0, 10, (2, 3))
    code_print(f"type: {type(i)}, i: {i}")

    st_code(code_print(f''))
### EndofCodeSection###

def py_np_math():
    a = np.array([3, 6, 9, 12])
    code_print(f"type: {type(a)}, a: {a}, a/3: {a/3}")

    st_code(code_print(f''))
### EndofCodeSection###

def py_np_copy_view():
    # the copy will not affect original array, but the view will
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.copy()
    y = arr.view()
    arr[0] = 42
    x[4] = 10
    y[4] = 10
    code_print(f"arr: {arr}, arr.base: {arr.base} \nx: {x}, x.base: {x.base}\ny: {y}, y.base: {y.base}")

    st_code(code_print(f''))
### EndofCodeSection###

def py_np_shape():
    # The shape returns a tuple with each index having the number of corresponding elements.
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    code_print(f"arr.shape: {arr.shape}")

    # reshaping
    code_print(f"\n--- reshaping ---")
    try:
        newarr = arr.reshape(4,3)
    except Exception as e:
        code_print(f"Error: {str(e)}")

    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    code_print(f"arr.reshape(4,3): {arr.reshape(4,3)}")

    # see copy or view
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    code_print(f"arr.reshape(2, 4).base: {arr.reshape(2, 4).base}") 

    code_print(f"\n--- pass -1 ---")
    # pass -1. the np will calculate for you
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    newarr = arr.reshape(2, 2, -1)
    code_print(f"newarr: {newarr}")
    st_code(code_print(f''))
### EndofCodeSection###

def py_np_loop():
    # other than normal loops as in lists

    code_print(f"\n--- nditer() ---")
    # nditer()
    arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    for x in np.nditer(arr):
        code_print(f"{x}")

    code_print(f"\n--- op_dtypes ---")
    arr = np.array([1, 2, 3])
    for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
        code_print(f"{x}")
    

    code_print(f"\n--- dimensions ---") 
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    for x in np.nditer(arr[:, ::2]):
        code_print(f"{x}")

    code_print(f"\n--- ndenumerate ---") 
    arr = np.array([1, 2, 3])
    for idx, x in np.ndenumerate(arr):
        code_print(f"idx: {idx} x: {x}") 

    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    for idx, x in np.ndenumerate(arr):
        code_print(f"idx: {idx} x: {x}") 

    st_code(code_print(f''))
### EndofCodeSection###  

def py_np_join():
    code_print(f"\n--- concatenate ---") 
    # array concat
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    # => array([1, 2, 3, 4, 5, 6])
    code_print(f"np.concatenate((a, b)): {np.concatenate((a, b))}")

    code_print(f"\n--- axis ---") 
    # axis
    a = np.array([[1, 2], [3, 4]])
    b = np.array([[5, 6], [7, 8]])
    arr = np.concatenate((a, b), axis=1)
    code_print(f"np.concatenate((a, b)): {np.concatenate((a, b))}")

    code_print(f"\n--- stack ---") 
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    code_print(f"np.stack((a, b)): {np.stack((a, b))}")             # this happens to be the same as vstack
    code_print(f"np.stack((a, b),axis=1): {np.stack((a, b), axis=1)}")


    code_print(f"\n--- hstack ---") 
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    code_print(f"np.hstack((a, b)): {np.hstack((a, b))}")

    code_print(f"\n--- vstack ---") 
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    code_print(f"np.vtack((a, b)): {np.vstack((a, b))}")

    code_print(f"\n--- dstack ---") 
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    code_print(f"np.dtack((a, b)): {np.dstack((a, b))}")
    st_code(code_print(f''))
### EndofCodeSection###  

def py_np_split():
    code_print(f"\n--- array_split() ---") 
    arr = np.array([1, 2, 3, 4, 5, 6])
    code_print(f"np.array_split(arr, 3): {np.array_split(arr, 3)}")
    code_print(f"np.array_split(arr, 4): {np.array_split(arr, 4)}")

    code_print(f"\n--- a2 dimensions ---") 
    arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
    newarr_a = np.array_split(arr, 3)
    newarr_b = np.array_split(arr, 3, axis=1)
    code_print(f"newarr_a: {newarr_a}, \nnewarr_b: {newarr_b}")

    code_print(f"\n--- hsplit() ---") 
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
    code_print(f"np.hsplit(arr, 3): {np.hsplit(arr, 3)}")

    st_code(code_print(f''))
### EndofCodeSection###  

def py_np_search():
    arr = np.array([1, 2, 3, 4, 5, 4, 4])
    code_print(f"np.where(arr == 4): {np.where(arr == 4)}")           # return a tuple for indices for value 4

    arr = np.array([10, 14, 93, 41, 8, 7])
    code_print(f"np.where(arr%2 == 1): {np.where(arr%2 == 1)}")       # return indices for all the odd

    code_print(f"\n--- searchsorted() ---") 
    arr = np.array([6, 7, 8, 9])
    code_print(f"np.searchsorted(arr, 7): {np.searchsorted(arr, 7)}") # Find the indexes where the value 7 should be inserted to keep the array sorted
    code_print(f"np.searchsorted(arr, 7, side='right'): {np.searchsorted(arr, 7, side='right')}") 

    arr = np.array([1, 3, 5, 7])
    code_print(f"np.searchsorted(arr, [2, 4, 6]): {np.searchsorted(arr, [2, 4, 6])}")  # return indices for multiple values to be inserted to keep the array sorted

    st_code(code_print(f''))
### EndofCodeSection### 

def py_np_sort():
    arr = np.array([3, 2, 0, 1])
    code_print(f"np.sort(arr): {np.sort(arr)}") 

    arr = np.array([[3, 2, 4], [5, 0, 1]])
    code_print(f"np.sort(arr): {np.sort(arr)}") 

    st_code(code_print(f''))
### EndofCodeSection###   

def py_np_filter():
    # Getting some elements out of an existing array and creating a new array out of them is called filtering.
    arr = np.array([41, 42, 43, 44])
    x = [True, False, True, False]
    code_print(f"arr[x]: {arr[x]}")       # the new array contains only the values where the filter array had the value True, in this case, index 0 and 2.

    filter_arr = arr > 42
    code_print(f"arr[filter_arr]: {arr[filter_arr]}") 
  
    st_code(code_print(f''))
### EndofCodeSection###  

def pynp_ref():
    code_print(f"https://https://www.w3schools.com/python/numpy/") 
    st_code(code_print(f''))
### EndofCodeSection###  
 



    




