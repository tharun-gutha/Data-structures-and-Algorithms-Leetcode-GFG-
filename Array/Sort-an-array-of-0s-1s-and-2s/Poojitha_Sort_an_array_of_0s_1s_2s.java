class Solution
{
    public static void sort012(int a[], int n)
    {
       int low=0;
       int high = n-1;
       int middle = 0,temp =0;
       while(middle <= high){
           switch(a[middle]){
               case 0:
                   temp = a[low];
                   a[low] = a[middle];
                   a[middle]=temp;
                   low++;
                   middle++;
                   break;
               case 1:
                   middle++;
                   break;
               case 2:
                   temp = a[middle];
                   a[middle]=a[high];
                   a[high]=temp;
                   high--;
                   break;
           }
       }
    }
}