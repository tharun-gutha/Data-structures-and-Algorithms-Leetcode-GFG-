/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var productExceptSelf = function(nums) {
  var l =1;
   var leftArr = [];
   for(i=0;i<nums.length;i++)
       {
           leftArr[i] = l;
           l*=nums[i];
       }
   var r=1;
   var rightArr = [];
   for(i=nums.length-1;i>=0;i--)
       {
           rightArr[i] = r;
           r*=nums[i];
           rightArr[i]*=leftArr[i];
       }
   return rightArr;
};

console.log(productExceptSelf([1,2,3,4]));