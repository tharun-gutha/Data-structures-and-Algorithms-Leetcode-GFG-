/**
 * @param {number[][]} matrix
 * @return {number[]}
 */
 var spiralOrder = function(matrix) 
 {
   var result = [];
   while(matrix.length)
   {
     var first = matrix.shift();
     result.push(...first);
     for(var m of matrix)
     {
        var value = m.pop()
        if(value)
        {
          result.push(value)
        }
       m.reverse();
     }
     matrix.reverse();
   }
   return result;
 }

 console.log(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]));