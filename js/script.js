
// var data = [3, 7, 2, 9, 1, 11];
// var sum = 0;
// data.forEach(function (d){
//   sum += d;
// })
// console.log('Sum: ' + sum);
//
// var names = ['Alice', 'Bob', 'Carol']
// names.forEach(function (n, i){
//   console.log(i + ': ' + n)
// })

// underscore
// var items = ['F', 'C', 'C', 'A', 'B', 'A', 'C', 'E', 'F']
// console.log(_.countBy(items))
//
// journeys = [
//   {period: 'morning', items: [44, 34, 56, 31]},
//   {period: 'evening', items: [35, 33],},
//   {period: 'morning', items: [33, 29, 35, 41]},
//   {period: 'evening', items: [24, 45, 27]},
//   {period: 'morning', items: [18, 23, 28]}
// ];
//
// var groups = _.groupBy(journeys, 'period');
// console.log(groups)
// var mTimes = _.pluck(groups['morning'], 'times');
// mTimes = _.flatten(mTimes);
// console.log(mTimes)
// var average = function (l) {
//   var sum = _.reduce(1, function (a, b) {
//     return a + b
//   }, 0);
//   return sum / l.length;
// };
// console.log('Average morning time is ' + average(mTimes));

// functional array method
// var nums = [1, 2, 3, 4, 5, 6]
// var nums2 = [1, 2, 3, 4, 5, 6]
// var sum = nums.filter(function (o) {
//   return o % 2
// })
//   .map(function (o) {
//     console.log(o)
//     return o * o
//   }).reduce(function (a, b) {
//     console.log(a + ', ' + b)
//     return a + b
//   });
// console.log(sum)

//DRY
// num = [1, 2, 4]
// var isOdd = function (x) {
//   return x % 2
// };
// sum = num.filter(isOdd)
// console.log(sum)

//closure
function Counter(inc){
  var count = 0;
  var api = {};
  api.add = function (){
    count+=inc;
    console.log(
      'Current count: ' + count);
  }

  api.sub = function (){
    count -= inc;
    console.log('Current count: ' + count);
  }

  api.reset = function(){
    count = 0;
    console.log('Count reset to 0')
  }
  return api;
}
cntr = Counter(3);
cntr.add()
cntr.add()
cntr.add()
cntr.sub()
cntr.reset()
