class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for p, h in enumerate(heights):
            start = p
            while(stack and h < stack[-1][0]):
                top_h, top_p = stack.pop()
                area = top_h*(p - top_p)
                max_area = max(area, max_area)                    
                start = top_p                                                                                                                            	    
            stack.append([h, start])

        for h, p in stack:
            max_area = max(max_area, h*(len(heights)-p))
        return max_area
