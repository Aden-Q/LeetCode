# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        res = []
        
        def serialize_util(root):
            nonlocal res
            if not root:
                return
            res.append(root.val)
            serialize_util(root.left)
            serialize_util(root.right)
            return
        
        serialize_util(root)
        return ' '.join(str(s) for s in res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        data = [int(s) for s in data.split()]
        
        def deserialize_util(data):
            if len(data) == 0:
                return None
            root = TreeNode(data[0])
            idx = 0
            while idx < len(data) and data[idx] <= data[0]:
                idx += 1
            root.left = deserialize_util(data[1:idx])
            root.right = deserialize_util(data[idx:])
            return root
            
        return deserialize_util(data)
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans