/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var sortedSquares = function(nums) {
  var arr = nums.map(sqr) //Passed a function sqr into map
  function sqr(num)
   {
       return Math.pow(num,2) //Here, each array item will be called and squared and the result is returned to arr
   }
   return arr.sort(function(a,b){return a-b}) //here, sorted array is returned to function
};
console.log(sortedSquares([0,2,1,5,4]));

/* Time complexity O(n) */
/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var sortedSquares = function(nums) {
    var len = nums.length
    var arr = new Array(len)
    var left = 0
      var right = len - 1
    for (let i = len - 1; i >= 0; i --) 
    {
        var leftAbs = Math.abs(nums[left]);
        var rightAbs = Math.abs(nums[right]);
        if (leftAbs >= rightAbs) 
        {
            arr[i] = leftAbs ** 2;
            left ++
        } 
        else
        {
            arr[i] = rightAbs ** 2;
            right --;
        }
    }
    return arr;
};

/* Another method
 var sortedSquares = function(nums) {
  for(var i in nums)
      {
          nums[i] = Math.pow(nums[i],2)
      }
  return nums.sort(function(a,b){return a-b})
};  */