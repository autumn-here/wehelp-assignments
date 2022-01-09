//Javascript Q1
function calculate(min, max) {
  let num = 0
  for ( let i = min; i <= max; i+=1) {
    num += i
  }
  console.log(num);
}

calculate(1, 3) //印出6
calculate(4, 8) //印出30

//Javascript Q2
function avg(data){
  let salary_sum = 0;
  for (let key in data["employees"]){
    salary_sum += data["employees"][key]["salary"]
  }
  let salary_avg = salary_sum / data["count"]
  console.log(salary_avg)
  }
  avg({
  "count":3,
  "employees":[
  {
  "name":"John",
  "salary":30000
  },
  {
  "name":"Bob",
  "salary":60000
  },
  {
  "name":"Jenny",
  "salary":50000
  }
  ]
  }); //印出46666.666666666664


  //Javascript Q3
function maxProduct(nums){
  let positive = 1;
  let negative = 1;
  
  let temp_ary = Array.from(nums)
  for (let i = 1; i<=2; i++){
    let min_num = Math.min(...temp_ary)
    let num_index = temp_ary.indexOf(min_num)
    temp_ary.splice(num_index, 1)
    negative *= min_num
  }
  
  temp_ary = Array.from(nums)
  for (let i = 1; i<=2; i++){
    let max_num = Math.max(...temp_ary)
    let num_index = temp_ary.indexOf(max_num)
    temp_ary.splice(num_index, 1)
    positive *= max_num
  }
  
  if (positive > negative){
    console.log(positive)
  }
  else {
    console.log(negative)
  }
}

maxProduct([5, 20, 2, 6]) // 得到 120
maxProduct([10, -20, 0, 3]) // 得到 30
maxProduct([-1, 2]) // 得到 -2
maxProduct([-1, 0, 2]) // 得到 0
maxProduct([-1, -2, 0]) // 得到 2



//javascript Q4
function twoSum(nums, target){
  for (let i = 0; i <= nums.length; i++){
    for (let j = 1; j<= nums.length; j++){
      let result = [];
      if (nums[i] + nums[j] == target){
        result.push(i)
        result.push(j)
        return(result)
        }
      }
    }
  }
  let result=twoSum([2, 11, 7, 15], 9);
  console.log(result); // show [0, 2] because nums[0]+nums[2] is 9

//javascript Q5
function maxZeros(nums){
  let record = [];
  let length = 0;
  for(let i = 0; i < nums.length; i++ ){
    if (nums[i] != 0){
      record.push(length);
      length = 0;
    } else if (nums[i] == 0 && i == (nums.length-1)){
      length += 1;
      record.push(length);
    } else{
      length += 1;
    }
  }
  console.log(Math.max(...record))
  }
  maxZeros([0, 1, 0, 0]); // 得到 2
  maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]); // 得到 4
  maxZeros([1, 1, 1, 1, 1]); // 得到 0
  maxZeros([0, 0, 0, 1, 1]) //得到 3