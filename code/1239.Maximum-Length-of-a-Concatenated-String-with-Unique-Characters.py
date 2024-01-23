class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = 0

        def dfs(curr, path) -> None:
            nonlocal ans
            ans = max(ans, len(path))

            if curr >= len(arr):
                return
            
            # for the current word, we can either add it to the set or skip it
            can_add = True
            for c in arr[curr]:
                if c in path:
                    can_add = False

            if len(arr[curr]) != len(set(arr[curr])):
                can_add = False
            
            if can_add:
                for c in arr[curr]:
                    path.add(c)
                dfs(curr+1, path)
                for c in arr[curr]:
                    path.remove(c)

            # skip the current word
            dfs(curr+1, path)

            return

        dfs(0, set())

        return ans            
