class Solution:
    def simplifyPath(self, path: str) -> str:
        # each element in the stack is a sub-path, starting with '/', followed by the directory name
        stack = []

        for sub_path in path.split('/'):
            if sub_path == '':
                # ignore empty path because it's an indicator of consecutive '/':
                continue
            elif sub_path == '..':
                if stack:
                    stack.pop()
            elif sub_path != '.':
                stack.append(sub_path)

        return '/' + '/'.join(stack)
