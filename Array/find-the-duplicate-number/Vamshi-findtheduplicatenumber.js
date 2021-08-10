//First method
/**
 * @param {number[]} nums
 * @return {number}
 */
 var findDuplicate = function(nums) {
  var len = nums.length;
   var arr = new Array(len);
   var number;
   for(var i of nums)
       {
           if(!arr[i])
               {
                   arr[i]=1;
               }
           else
               {
                   number = i;
                   break;
               }
       }
   return number;
};

console.log(findDuplicate([1,3,4,2,2]));

/**
 * @param {number[]} nums
 * @return {number}
 */
 var findDuplicate = function(nums) {
  var obj = {};
  for(var i of nums)
      {
          if(!obj[i])
              {
                  obj[i] = 1;
              }
          else
              {
                  obj[i]+=1;
              }
      }
  for([key,value] of Object.entries(obj))
      {
          if(value>=2)
              {
                  return key;
              }
      }
};

console.log(findDuplicate([1,3,4,2,2]));
