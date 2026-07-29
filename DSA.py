""" Problem Statement:TWO SUM
planning to create a Two sum problem solution in BF approach and Optimal Approach 
"""

class DSA:
    def TwoSum(num,target):
        sum = 0 
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                if num[i]+num[j] == target:
                    return i,j
               
               
        
    # Two Pointer Approach (Only work when Array is sorted)
    def optimal_solution(num,target):
        start = 0 
        end = len(num) - 1 
        sum = 0
        while start < end :
            sum = num[start] + num[end]
            if sum == target:
                return start,end
            elif sum < target:
                start +=1
            else:
                end -=1
                
                
    def optimal_solution_hashmap(num,target):
        # dictionary to store {key,value}
        hash = {}
        
        for i , current_num in enumerate(num):
            needed_num = target - current_num
            if needed_num in hash:
                 return hash[needed_num],i
            hash[current_num] = i 
        
        return None
    def main():
        num = [2, 70,11,15]
        target = 9
        print(DSA.optimal_solution_hashmap(num,target))
        
        
DSA.main()    
