////////////////////////////// Traditinal Way ////////////////////////////////////////////////
  
// k = [50, 20, 30, 400, 5, -5, -3]


// var maxNum = function(array) {
//   element = array[0];
//   for (var i = 0; i < array.length; i++) {
//     if (array[i] > element) {   // just change the less then sign to greater and
//                                 // vice versa to find min and max (array[i] < mxn)=> for minimum and (array[i> mxn=> for maximum])
//       element = array[i];
//     }
//   }
//   console.log(element);
// };

// maxNum(k);

 ////////////////////////////////////////////////////////// Using For Each /////////////////////////////////////////////////////////////

k=[1,2,3,4,5,44,332,9982]
var maxNum2 = function(array) {
    max = 0;
    k.forEach(function(element){
      if (element > max) {
        max = element;
      }
    })
    console.log(max);
  };
  
  maxNum2(k);



