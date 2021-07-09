class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        
        '''
        first method - sort the elements and return arr[k-1]
        arr.sort()
        return arr[k-1]

        time complexity - o(nlogn)
        '''
        
        #second method - find min element and remove till the kth min element is found and returned
        m=min(arr)
        for i in range(k-1):
            arr.remove(m)
            m=min(arr)
        return m   