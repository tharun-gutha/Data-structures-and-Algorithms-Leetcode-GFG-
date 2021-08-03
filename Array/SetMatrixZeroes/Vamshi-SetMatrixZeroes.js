/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
 var setZeroes = function(matrix) {
    var rows = [];
    var cols = [];
    for(var i=0;i<matrix.length;i++)
    {
      for(var j=0;j<matrix[i].length;j++)
      {
        if(matrix[i][j]==0)
        {
          rows.push(i);
          cols.push(j);
        }
      }
    }
    for(var i=0;i<matrix.length;i++)
    {
      for(var j=0;j<matrix[i].length;j++)
      {
        if((rows.includes(i)) || (cols.includes(j)))
        {
          matrix[i][j]=0;
        }
      }
    }
    return matrix;
};

console.log(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]));