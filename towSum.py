class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       
       arrayNumsTarget=[]

       for idx,i in enumerate(nums):
           def filterNums(item):
            return item != i
           
           filtered=nums.copy()

           del filtered[idx]



           for i2 in filtered:
              if(i + i2 == target):
                 arrayNumsTarget.append(idx)

       print(arrayNumsTarget)          

       return arrayNumsTarget    


Solution.twoSum("a", [3,2,4], 6)