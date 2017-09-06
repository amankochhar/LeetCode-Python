class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height) - 1
        l,r = 0, length
        maxWater = length * min(height[0], height[length])
        for i in range(length):
            if height[l] >= height[r]:
                # calculate the max water
                maxWater = max(maxWater, min(height[l], height[r]) * (r-l))
                #move right in
                r -= 1
            else:
                # calculate the max water
                maxWater = max(maxWater, min(height[l], height[r]) * (r-l))                
                #move left in
                l += 1
        return maxWater