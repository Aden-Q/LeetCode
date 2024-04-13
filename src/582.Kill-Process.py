class TreeNode:
    def __init__(self, val):
        self.val = val
        self.children = []

class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        # a map from node ID to its TreeNode
        node_map = defaultdict(int)

        for p in pid:
            node_map[p] = TreeNode(p)
        
        # set parent
        for i in range(len(pid)):
            if ppid[i] == 0:
                # this node has no parent
                continue
            # we just add the id to it
            node_map[ppid[i]].children.append(pid[i])

        # now we run dfs from the node to be killed, impossible to visit the same node twice
        nodes_to_kill = []
        def dfs(node_id):
            nonlocal nodes_to_kill
            nodes_to_kill.append(node_id)
            
            for next_node_id in node_map[node_id].children:
                dfs(next_node_id)

            return

        dfs(kill)
        return nodes_to_kill
