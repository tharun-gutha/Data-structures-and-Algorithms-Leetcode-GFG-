/**
 * @param {number[]} nums
 * @return {number}
 */
 var singleNumber = function(nums) {
   var obj = {}
   for(var i of nums)
   {
     if(obj[i])
     {
       obj[i]=false
     }
     else
     {
       obj[i]=true
     }
   }
   for([key,value] of Object.entries(obj))
   {
     if(value)
     {
       return key
     }
   }
};
console.log(singleNumber([1,2,2]))