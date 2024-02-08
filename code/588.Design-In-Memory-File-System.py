class File:
    def __init__(self, path, isDir = False):
        # path is the relative path input, relative only to its parent level
        # for example for a path '/a/b', path is just 'b'
        self.path = path
        # isDir indicates whether the current file is a file or a directory
        self.isDir = isDir
        self.content = []
        # implemented as a trie
        self.children = {}

class FileSystem:

    def __init__(self):
        # the root directory
        self.root = File('/', isDir=True)

    def ls(self, path: str) -> List[str]:
        if path == '/':
            # a special case
            return sorted([child for child in self.root.children])

        curr = self.root
        # similarly we do a traversal to find the target node first
        path = path.split('/')
        for i in range(1, len(path)):
            curr = curr.children[path[i]]
        
        # if the target is a file, only return it
        if not curr.isDir:
            return [curr.path]

        # otherwise we list all contents in the current directory
        return sorted([child for child in curr.children])

    def mkdir(self, path: str) -> None:
        curr = self.root
        path = path.split('/')
        # ignore the root dir, and make dirs iteratively until the end
        for i in range(1, len(path)):
            if path[i] in curr.children:
                curr = curr.children[path[i]]
            else:
                # only create when the dir does not exist
                curr.children[path[i]] = File(path[i], isDir=True)
                curr = curr.children[path[i]]
        # for '/a/b' in the end we have something like this:
        # '/' -> 'a' -> 'b' 

    def addContentToFile(self, filePath: str, content: str) -> None:
        curr = self.root
        path = filePath.split('/')
        # first navigate to the target directory
        for i in range(1, len(path) - 1):
            curr = curr.children[path[i]]
        # check whether the file exists in the target directory
        file = path[-1]
        if file in curr.children:
            # exists, append the content to the file
            curr.children[file].content.append(content)
        else:
            # does not exist, create the file and append the content to it
            f = File(file, isDir=False)
            f.content.append(content)
            curr.children[file] = f

    def readContentFromFile(self, filePath: str) -> str:
        curr = self.root
        path = filePath.split('/')
        # navigate to the target file
        for i in range(1, len(path)):
            curr = curr.children[path[i]]
        
        return ''.join(curr.content)

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)