

def merge(array, p, q, r, byfunc=None):
    nleft = q - p +1
    nright = r - q
    left_array = array[p:q+1]
    right_array = array[q+1:r+1]
    left = 0
    right = 0
    dest = p
    
    while left<nleft and right<nright:
        compare_leq = None
        if byfunc == None:
            compare_leq = left_array[left]<=right_array[right]
        else:
            compare_leq = byfunc(left_array[left])<=byfunc(right_array[right])

        if compare_leq:
            array[dest] = left_array[left]
            left += 1
            dest += 1
        
        else:
            array[dest] = right_array[right]
            right += 1
            dest += 1
    
    while left<nleft:
        array[dest] = left_array[left]
        left += 1
        dest += 1
    while right<nright:
        array[dest] = right_array[right]
        right += 1
        dest += 1

def mergesort_recursive(array, p, r, byfunc=None):
    if r -p >0:
        q = int((p+r)/2)
        mergesort_recursive(array,p,q,byfunc)
        mergesort_recursive(array,q+1,r,byfunc)
        merge(array,p,q,r,byfunc)
        

def mergesort(array, byfunc=None):
    mergesort_recursive(array,0,len(array)-1,byfunc)

class Stack:
  pass

class EvaluateExpression:
  pass


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





