/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var findDuplicates = function(nums) {
  var res = [];
  var m = new Map();
  for(var i=0;i<nums.length;i++)
      {
          if(!m.has(nums[i]))
              {
                  m.set(nums[i],1);
              }
          else
              {
                  res.push(nums[i]);
              }
      }
  return res;
};

console.log(findDuplicates([1,1,2]));