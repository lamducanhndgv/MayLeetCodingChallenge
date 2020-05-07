class Solution:
    def isCousins(self, root: TreeNode, x: int, y:int):
        if root.val == x or root.val == y:
            return False
        
        def check(iX, iY):
            return iX != -1 and iY != -1

        def Tree_BFS(rTree: TreeNode):
            info_x = -1
            info_y = -1

            queue = collections.deque()
            queue.append((-1, 0, root))

            while len(queue):
                p, d, node = queue.popleft()

                if node.val == x:
                    info_x = (p, d)

                if node.val == y:
                    info_y = (p, d)

                if node.left:
                    queue.append((node.val, d + 1, node.left))
                if node.left:
                    queue.append((node.val, d + 1, node.right))

                if check(info_x, info_y):
                    break
            if check(info_x, info_y):
                return (info_x[0] != info_y[0]) and (info_x[1] == info_y[1])
            return False
        return Tree_BFS(root)
