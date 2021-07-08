/**
 * @param {number[]} nums
 * @return {boolean}
 */
 var canBeIncreasing = function(nums) {
  var count=0
  for(var i =1;i<nums.length;i++)
      {
          if(nums[i]<=nums[i-1])
          {
              if(count==1)
              {
                  return false
              }
              count++
              if(i>1&&nums[i]<=nums[i-2])
              {
                  nums[i]=nums[i-1]
              }
          }
      }
  return true
};
console.log(canBeIncreasing([2,1,3,2]))