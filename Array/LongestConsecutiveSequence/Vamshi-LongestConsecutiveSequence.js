/**
 * @param {number[]} nums
 * @return {number}
 */
 var longestConsecutive = function(nums) {
  if(nums==null || nums.length===0)
  {
    return 0;
  }
  var max = 0;
  var set = new Set(nums);
  for(var num of set)
  {
    if(set.has(num-1))
    {
      continue;
    }
    var currentNum = num;
    var currentMax = 1;
    while(set.has(currentNum+1))
    {
      currentNum++;
      currentMax++;
    }
    max = Math.max(max,currentMax);
  }
  return max;
};

console.log(longestConsecutive([100,4,200,3,2]));