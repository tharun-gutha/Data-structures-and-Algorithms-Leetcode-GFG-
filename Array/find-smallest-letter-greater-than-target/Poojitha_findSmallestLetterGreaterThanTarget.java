class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int n = letters.length;
        if(target >= letters[n-1]){
            return letters[0];
        }
        
       int low = 0, high = letters.length - 1;
      
        int duplicate = -1;
        
        while (low <= high)
        {
           
            int mid = (low + high) / 2;
            if (letters[mid] > target)
            {
                high = mid - 1;
                duplicate = mid;
            }
            else
                low = mid + 1;
            }
 
        return letters[duplicate];
        }
}
