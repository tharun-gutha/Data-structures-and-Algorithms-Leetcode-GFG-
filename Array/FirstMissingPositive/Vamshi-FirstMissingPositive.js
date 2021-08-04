/**
 * @param {number[]} nums
 * @return {number}
 */
 var firstMissingPositive = function(nums) {
  var m = new Map();
  for(var i=0;i<nums.length;i++)
      {
          m.set(nums[i],true);
      }
  for(var i=1;i<=nums.length;i++)
      {
          if(!m.has(i))
              {
                  return i;
              }
      }
  return nums.length+1;
};

console.log(firstMissingPositive([1,2,0]));