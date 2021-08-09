/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
 var nextGreatestLetter = function(letters, target) {
  var start = 0;
  var end = letters.length-1;
  var result = letters[0];
  while(start<=end)
      {
          var mid = Math.floor((start+end)/2);
          if(target==letters[mid])
              {
                  start = mid+1;
              }
          else if(target>letters[mid])
              {
                  start = mid+1;
              }
          else
              {
                  result = letters[mid];
                  end = mid-1;
              }
      }
  return result;
};

console.log(nextGreatestLetter(["c","f","j"],"c"));

/*another method */
/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
 var nextGreatestLetter = function(letters, target) {
  var len = letters.length;
  if((target<letters[0]) || (target>letters[len-1]) || (target==letters[len-1]))
      {
          return letters[0];
      }
  else
      {
          var arr = letters.filter(check);
          function check(letter)
          {
              return letter>target;
          }
          return arr[0];
      }
};

console.log(nextGreatestLetter(["c","f","j"],"c"));

//another method

/**
 * @param {character[]} letters
 * @param {character} target
 * @return {character}
 */
 var nextGreatestLetter = function(letters, target) {
  var len = letters.length;
          for(var i=0;i<len;i++)
              {
                  if(target<letters[i])
                      {
                          return letters[i];
                      }
              }
  return letters[0];
};

console.log(nextGreatestLetter(["c","f","j"],"c"));
