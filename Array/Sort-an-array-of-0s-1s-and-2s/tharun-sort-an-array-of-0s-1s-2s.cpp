 // it is an algorithm called dutch national flag . we will take three pointers low, mid and high .based on the conditon we will swap and increment the pointers. 
class Solution
 {
   public:
    void sort012(int a[], int n)
    {
        // coode here 
        int l=0,m=0,h=n-1;//take 3 pointer low mid high and based on the condition we will swap and one more thing if we are asked to solve inplace that means without extra space go for swapping.
        while(m<=h)
        {
            if(a[m]==0)
            {
                swap(a[m],a[l]);
                l++;
                m++;
            }
            else if(a[m]==1)
            {
                m++;
            }
            else if(a[m]==2)
            {
                swap(a[m],a[h]);
                h--;
            }
        }
        
    }
 }
 

 //time complexity O(n)