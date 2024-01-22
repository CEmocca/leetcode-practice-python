

class Solution:

    def __init__(self):
        pass

    # time complexity is O(N)
    # space complexity is O(N)
    def max_width_of_vertical_area(self, points: list[list[int]]) -> int:
        
        x_axis = sorted(map(lambda point: point[0], points)) # desc sorted
        
        diff_results = []
        i = 1
        while i < len(x_axis):
            diff_results.append(x_axis[i] - x_axis[i - 1])
            i += 1
            
        # select max number out of array
        ans = max(diff_results)
        
        return ans
    

solution = Solution()

# [x, y]
# considering only x -> 8, 9, 7 ,9
# sorted x = 7, 8, 9, 9
# minus each pair: 8-7 = 1, 9-8 = 1, 9-9 = 0 -> [1, 1, 0]
# max width is 1
print(solution.max_width_of_vertical_area([[8,7],[9,9],[7,4],[9,7]]))


# [x, y]
# considering only x -> 3, 9, 1, 1, 5, 8
# sorted x = 1, 1, 3, 5, 8, 9
# minus each pari: 1 - 1 = 0, 3 - 1 = 2, 5 - 3 = 2, 8 - 5 = 3, 9 - 8 = 1 -> [0, 2, 2, 3, 1]
# max width is 3
print(solution.max_width_of_vertical_area([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))