

"""
    This module contains a set of sorting algorithms 
    for user's choice.

    Algorithms available:


            1. bubble
            2. selection
            3. merge
            4. quick (pivot chosen to be the middle of list)
            5. shell
            6. heap

            7. sorting_algorithm - This function encapsulates all of the 
                                   algorithms above


"""



def bubble_sort(seq):
    """Inefficiently sort the mutable sequence (list) in place.
       seq MUST BE A MUTABLE SEQUENCE.
 
       As with list.sort() and random.shuffle this does NOT return 
    """
    changed = True
    while changed:
        changed = False
        for i in xrange(len(seq) - 1):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
                changed = True
    return seq



def selection_sort(lst):
    for i, e in enumerate(lst):
        mn = min(range(i,len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e
    return lst


 
def merge_sort(m):
    if len(m) <= 1:
        return m
 
    middle = len(m) // 2
    left = m[:middle]
    right = m[middle:]
 
    left = merge_sort(left)
    right = merge_sort(right)
    return list(merge(left, right))




def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result




def qsort(list):
    if not list:
        return []
    else:
        pivot = list[0]
        less = [x for x in list     if x <  pivot]
        more = [x for x in list[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(more)




def quick_sort(list,pos_piv):
    if not list:
        return []
    else:
        if pos_piv == 'last':
            pivot = list[len(list)-1]
        elif pos_piv == 'first':
            pivot = list[0]
        elif pos_piv == 'middle':
            pivot = list[len(list)/2]


        less = [x for x in list     if x <  pivot]
        more = [x for x in list[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(more)


 
def shell_sort(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)
    return seq



def heap_sort(lst):
  ''' Heapsort. Note: this function sorts in-place (it mutates the list). '''
 
  
  for start in range((len(lst)-2)/2, -1, -1):
    siftdown(lst, start, len(lst)-1)
 
  for end in range(len(lst)-1, 0, -1):
    lst[end], lst[0] = lst[0], lst[end]
    siftdown(lst, 0, end - 1)
  return lst
 

def siftdown(lst, start, end):
  root = start
  while True:
    child = root * 2 + 1
    if child > end: break
    if child + 1 <= end and lst[child] < lst[child + 1]:
      child += 1
    if lst[root] < lst[child]:
      lst[root], lst[child] = lst[child], lst[root]
      root = child
    else:
      break




def sorting_algorithm(x,sorting_method):
    if (sorting_method=='bubble'):
        y = bubble_sort(x)
    elif (sorting_method=='selection'):
        y = selection_sort(x)
    elif (sorting_method=='merge'):
        y = merge_sort(x)
    elif (sorting_method=='quick'):
        position_pivot = 'middle'
        y = quick_sort(x,position_pivot)
    elif (sorting_method=='shell'):
        y = shell_sort(x)
    elif (sorting_method=='heap'):
        y = heap_sort(x)

    return y 