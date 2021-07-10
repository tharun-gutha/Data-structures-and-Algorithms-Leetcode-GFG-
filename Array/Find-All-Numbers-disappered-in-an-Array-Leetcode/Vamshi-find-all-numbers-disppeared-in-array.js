/*First method */
/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var findDisappearedNumbers = function(nums) {
  var result = []
  for(var i=0;i<nums.length;i++)
      {
          var num=Math.abs(nums[i])
          var index = num-1
          nums[index]=Math.abs(nums[index])*-1
      }
    for(var j=0;j<nums.length;j++)
        {
            if(nums[j]>0)
                {
                    result.push(j+1)
                }
        }
    return result
};

/*another method*/
/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var findDisappearedNumbers = function(nums) {
  var arr = []
  for(var i=1;i<=nums.length;i++)
    {
        if(!nums.includes(i))
            {
                arr.push(i)
            }
    }
    return arr
};

/* one more method*/
/**
 * @param {number[]} nums
 * @return {number[]}
 */
 var findDisappearedNumbers = function(nums) {
  var arr = []
  for(var i=1;i<=nums.length;i++)
    {
        arr.push(i)
    }
    var res = arr.filter(x => !nums.includes(x));
    return res
};