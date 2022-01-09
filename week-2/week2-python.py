#python Q1

def calculate(min, max):
    num = 0
    for i in range(min, max+1):
        num += i
    print(num)

calculate(1, 3) # 印出 6
calculate(4, 8) # 印出 30


#python Q2

def avg(data):
    salary_sum = 0
    for i in range(data["count"]):
        salary_sum += data["employees"][i]["salary"]
    salary_avg = salary_sum / data["count"]
    print(salary_avg)

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
}) # 印出46666.666666666664


#Python Q3
#最大乘積可能是最大的兩個正數or最小的兩個負數相乘
#故找出list中最大和最小的兩個數字的乘積來比較

def maxProduct(nums):
    positive = 1
    negative = 1
    
    temp = nums.copy()
    for i in range(2):
        min_num = min(temp)
        negative *= min_num
        temp.remove(min_num)
        
    temp = nums.copy()
    for i in range(2):
        max_num = max(temp)
        temp.remove(max_num)
        positive *= max_num
        
    if positive > negative:
        print(positive)
    else:
        print(negative)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([-1, -2, 0]) # 得到 2


#python Q4
def twoSum(nums, target):
    result = []
    for i in range(len(nums)):
        if nums[i] > target:
            pass
        else:
            temp_sum = 0
            for j in range (i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    return result

# your code here
result=twoSum([2, 11, 7, 15], 9)
print(result) # 印出[0, 2]


#python Q5
def maxZeros(nums):
    record = []
    length = 0
    for i in nums:
        if i != 0:
            record.append(length)
            length = 0
        else:
            length += 1
            if i == nums[-1]:
                record.append(length)
            else:
                continue
    print(max(record))
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4 
maxZeros([1, 1, 1, 1, 1]) # 得到 0 
maxZeros([0, 0, 0, 1, 1]) # 得到 3
