/**
 * @param {number[]} nums
 * @return {boolean}
 */
/* one method */
var containsDuplicate = function(nums) {
  var set = new Set()
  for(var i of nums)
  {
    if(set.has(i))
    {
      return true
    }
    set.add(i)
  }
  return false
};
console.log(containsDuplicate([1,1,3,4]));

/* another method */
// var containsDuplicate = function(nums) {
//   var arr = []
//   for(var i in nums)
//   {
//     if(arr.includes(nums[i]))
//     {
//       return true
//     }
//     arr[i]=nums[i]
//   }
//   return false
// };
// console.log(containsDuplicate([1,2,1]));
