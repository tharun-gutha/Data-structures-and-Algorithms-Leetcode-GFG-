var sort012 = function(arr, N)
{
    var a= []
    var b= []
    var c= []
    for(var i of arr)
    {
        if(i==0)
        {
            a.push(i)
        }
        else if(i==1)
        {
            b.push(i)
        }
        else if(i==2)
        {
            c.push(i)
        }
    }
  return a.concat(b,c)
}
console.log(sort012([0,2,1,1,2,0],6))

// var sort012 = function(arr,N)
// {
//   return arr.sort(function(a,b){return a-b})
// }
// console.log(sort012([0,2,1,1,2,0],6))
