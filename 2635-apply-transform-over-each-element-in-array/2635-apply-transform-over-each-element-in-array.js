/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    
    return arr.map((value, index) => fn(value, index));
};



// /**
//  * @param {number[]} arr
//  * @param {Function} fn
//  * @return {number[]}
//  */
// // var map = function(arr, fn) {
//     let result = [];

//     for (let i = 0; i < arr.length; i++) {
//         result.push(fn(arr[i], i));
//     }

//     return result;
// };