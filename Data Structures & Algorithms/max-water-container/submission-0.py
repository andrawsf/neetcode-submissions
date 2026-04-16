class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftBar, rightBar = 0, len(heights) - 1
        maxArea = 0

        while leftBar < rightBar:
            base = rightBar - leftBar
            height = 0
            #print("checking ", leftBar, " and ", rightBar, " with base ", base)

            # adjust height if right is taller
            if heights[rightBar] > heights[leftBar]:
                height = heights[leftBar]
                leftBar += 1
            else: 
                height = heights[rightBar]
                rightBar -= 1
            
            # check if this is max area
            area = base * height
            if area > maxArea:
                #print("Updating max to ", area)
                maxArea = area

        return maxArea



        