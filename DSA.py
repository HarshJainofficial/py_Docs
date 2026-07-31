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
    # def Optimal_solution_SWC(num,k):
    #     n = len(num) - 1 
    #     sum = 0
    #     for i in range(k):
    #         sum +=num[i]
    #         maxSum  = sum
    #     # print(sum)  
          
    #     for j in range(k,n):
    #         sum = sum - num[j-k] + num[j] 
    #         maxSum = max(sum ,maxSum )
    #     return maxSum
    
    # def BF_solution_Sliding_window(num,k):
    #     sum = 0
        
    #     n = len(num) - 1 
    #     for i in range(n-k+1):
    #         maxSum = 0
    #         for j in range(k):
    #             sum +=num[i+j]
    #             maxSum = max(sum,maxSum)
    #     return maxSum
                
   
    
    # def Optimal_solution_SWC_avg(num,k):
    #         n = len(num) - 1 
    #         sum = 0
    #         for i in range(k):
    #             sum +=num[i]
    #             maxSum  = sum
    #         # print(sum)  
              
    #         for j in range(k,n):
    #             sum = sum - num[j-k] + num[j] 
    #             maxSum = max(sum ,maxSum )
                
    #         return maxSum/k
    
    def Prefix_sum(num,k):
            sum=  num[0]
            for i in range(1,k):
                sum += num[i]
            return sum
        
    # Greedy Algorithm Technique
    
    def Greedy_algorithm(n,s):
        if s>n*9:
            return -1
        result = []
        # digit.append(str(9))
        # digit.append(str(9))
        # digit.append(str(5))
        # digit.append(str(0))
        # digit.append(str(0))
        # print ("".join(digit))
        
        for _ in range(n):
            digit = min(9,s)
            result.append(str(digit))
            s -= digit
        
        return "".join(result)
        # if s > 9*n:
        #     return -1 
        
        # for i in range(n):
        #     digit = min()
        
        
 
    
    def main():
        num = [1,12,-5,-6,50,3]
        k = 4
        # target = 9
        n,s =2,9
        print(DSA.Greedy_algorithm(n,s))
        
        
DSA.main()    
