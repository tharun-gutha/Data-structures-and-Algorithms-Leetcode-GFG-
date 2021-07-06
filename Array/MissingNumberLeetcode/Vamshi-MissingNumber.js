/**
 * @param {number[]} nums
 * @return {number}
 */
/*one method*/
 var missingNumber = function(nums) {
   var n =nums.length
   var sum = nums.reduce(getSum,0)
   function getSum(total,num)
   {
     return total+num
   }
   var add = n*(n+1)/2

   return add - sum
};
console.log(missingNumber([0,2,3]))

/* second method 
  var missingNumber = function(nums) {
  // for(i=0;i<=nums.length;i++)
  //   {
  //     if(nums.includes(i)!==true)
  //     {
  //       return i
  //     }
  //   }
   };
console.log(missingNumber([1]))
  */
