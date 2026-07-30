""" Problem Statement:TWO SUM
planning to create a Two sum problem solution in BF approach and Optimal Approach 
"""

class DSA:
    # def TwoSum(num,target):
    #     sum = 0 
    #     for i in range(len(num)):
    #         for j in range(i+1,len(num)):
    #             if num[i]+num[j] == target:
    #                 return i,j
               
               
        
    # Two Pointer Approach (Only work when Array is sorted)
    # def optimal_solution(num,target):
    #     start = 0 
    #     end = len(num) - 1 
    #     sum = 0
    #     while start < end :
    #         sum = num[start] + num[end]
    #         if sum == target:
    #             return start,end
    #         elif sum < target:
    #             start +=1
    #         else:
    #             end -=1
                
                
    # def optimal_solution_hashmap(num,target):
    #     # dictionary to store {key,value}
    #     hash = {}
        
    #     for i , current_num in enumerate(num):
    #         needed_num = target - current_num
    #         if needed_num in hash:
    #              return hash[needed_num],i
    #         hash[current_num] = i 
        
    #     return None
    
    
    # Problem Statement for Most water container 
    # def BF_approach_MWC(num):
    #     max_water = 0 
    #     n = len(num) - 1
    #     for i in range(n):
    #         for j in range(i+1,n):
    #             width = j - i 
    #             current_height = min(num[i],num[j])
    #             current_area = current_height*width
    #             if max_water < current_area:
    #                 max_water = current_area
    #     return max_water        
        
    # def Optimal_approach_MWC(num):
    #     left = 0
    #     right = len(num) - 1 
    #     max_water = 0
    #     while left < right:
            
    #         width = right - left
    #         current_height = min(num[left], num[right])
    #         current_area = current_height*width
    #         if max_water < current_area:
    #             max_water = current_area
    #         if num[left] < num[right]:
    #            left += 1
    #         else:
    #             right -=1
                
    #     return max_water 
    
    # Sliding Window Concept
    def Optimal_solution_SWC(num,k):
        n = len(num) - 1 
        sum = 0
        for i in range(k):
            sum +=num[i]
            maxSum  = sum
        # print(sum)  
          
        for j in range(k,n):
            sum = sum - num[j-k] + num[j]
            maxSum = max(sum ,maxSum )
        return maxSum
 
    
    def main():
        num = [2, 1, 5, 1, 3, 2]
        k = 3
        # target = 9
        print(DSA.Optimal_solution_SWC(num,k))
        
        
DSA.main()    
