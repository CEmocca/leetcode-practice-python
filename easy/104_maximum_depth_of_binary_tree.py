
from collections import deque
from typing import Optional

import sys
from os.path import dirname, abspath
dir = dirname(dirname(abspath(__file__)))
sys.path.append(dir)

from utils.tree import TreeNode

class Solution:
    
        
    def maxDepth_dfs(self, root: Optional[TreeNode]) -> int:
        
        def dfs(lroot: Optional[TreeNode], max_depth: int):
            if not lroot:
                return max_depth
            else:
                return max(dfs(lroot.left, max_depth + 1), dfs(lroot.right, max_depth + 1))
            
        return dfs(root, 0)
                    
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        
        queue.append([root, 0])
        
        max_depth = 0
        
        while queue:
            cur, depth = queue.popleft()
            if not cur:
                continue
            
            depth += 1
            max_depth = depth  
                
            if cur.left:
                queue.append([cur.left, depth])
            if cur.right:
                queue.append([cur.right, depth])
                
        return max_depth
            