class Solution:
    def maxArea(self, height: List[int]) -> int:
         max = 0
         for index,value in enumerate(height):
            for j in range(index+1, len(height)):
                m = min(value, height[j]) * (j-index)
                if(m > max):
                    max = m

                    
        