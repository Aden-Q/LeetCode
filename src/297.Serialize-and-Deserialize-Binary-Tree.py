# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def serialize_util(root):
            nonlocal res
            if not root:
                res.append(-1001)
                return
            res.append(root.val)
            serialize_util(root.left)
            serialize_util(root.right)
            return
            
        serialize_util(root)
        return ' '.join(str(val) for val in res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        from collections import deque
        data = list(map(int, data.split()))
        data = deque(data)
        def deserialize_util():
            nonlocal data
            if len(data) == 0:
                return None
            if data[0] == -1001:
                data.popleft()
                return None
            root = TreeNode(data[0])
            data.popleft()
            root.left = deserialize_util()
            root.right = deserialize_util()
            return root
            
        return deserialize_util()
            
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))