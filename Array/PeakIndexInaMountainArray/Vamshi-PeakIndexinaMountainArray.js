/**
 * @param {number[]} arr
 * @return {number}
 */
 var peakIndexInMountainArray = function(arr) {
  var start = 0;
  var end = arr.length-1;
  while(start<=end)
      {
          var mid = Math.floor((start+end)/2);
          if(arr[mid-1]<arr[mid] && arr[mid]>arr[mid+1])
              {
                  return mid;
              }
          else if(arr[mid-1]>arr[mid])
              {
                  end = mid-1;
              }
          else
              {
                  start = mid+1;
              }
      }
};

console.log(peakIndexInMountainArray([0,1,2,0]));

//Another method

/**
 * @param {number[]} arr
 * @return {number}
 */
 var peakIndexInMountainArray = function(arr) {
  return arr.indexOf(Math.max(...arr));
};

console.log(peakIndexInMountainArray([0,1,2,0]));
