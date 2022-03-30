def quicShort(array):
    if len(array) < 2:
        return array
    else:
         pivot = array[0]
         less = [i for in array[i:] if i <= pivot]
         greater = [i for i in array[i:] if i > pivot]
         return quicShort(less)+[pivot]+quicShort(greater)
     print quicShort([10,5,2,4])


      