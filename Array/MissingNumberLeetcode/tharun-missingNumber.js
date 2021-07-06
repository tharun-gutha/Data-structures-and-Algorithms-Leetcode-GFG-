/**
 * @param {number[]} nums
 * @return {number}
 */
 var missingNumber = function(nums) {

  let n=nums.length;
  let totalSum=(n*n+n)/(2);
  let arraySum=0;
  for(let i=0;i<n; i++){
      arraySum=arraySum+nums[i];
  }
  return totalSum-arraySum;
};