var twoSum = function(nums,target) {
  var arr = [];
  for(var i in nums)
  {
    if(arr.includes(target-nums[i]))
    {
      return [arr.indexOf(target-nums[i]),parseInt(i)]
    }
    else
    {
      arr[i]=nums[i];
    }
  }
};
console.log(twoSum([3,2,4],6))