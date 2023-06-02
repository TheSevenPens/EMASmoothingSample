# Demo of exponential moving average

# build data
data1 = [ 10, 12, 15, 17, 20, 23, 25, 27, 30, 33, 35 ] 
data2 = [ 35, 33, 30, 27, 25, 23, 20, 17, 15, 12, 10 ] 

# add tails of non-changing values at the end
tailsize = 40
data1 = data1 + (tailsize * [data1[-1]])
data2 = data2 + (tailsize * [data2[-1]])

# linear interpolation function

def lerp( a , b, alpha ) : 
    return ( a*(1-alpha)) + (b*alpha)


# Smoothing should be in range 0.0 to 1.0
# In practice, 1.0 is useless
# 0.0 means no smoothing

smoothing = 0.90

def run_smoothing(data) :
    # NOTE: Important that value_old and value_cur remain af floating point
    # truncating or rounding them will accumulate an error
    # the the value smoothed value will never converge when the input stays constant
    value_old = data[0]
    seq = 1
    for value_raw in data:
        value_cur = lerp(value_raw, value_old, smoothing)          
        value_cur_adjusted = round(value_cur) # rounding to an int
        
        print(f"SEQ:{seq} | INPUT:{value_raw} | OLD:{value_old:.3f} | CUR:{value_cur:.3f} | CURADJ:{value_cur_adjusted}")      
        value_old = value_cur
        seq+=1
        
run_smoothing(data1)
run_smoothing(data2)