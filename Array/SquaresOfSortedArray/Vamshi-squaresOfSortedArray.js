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

/* Another method
 var sortedSquares = function(nums) {
  for(var i in nums)
      {
          nums[i] = Math.pow(nums[i],2)
      }
  return nums.sort(function(a,b){return a-b})
};  */