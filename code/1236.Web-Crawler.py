# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        # a helper function to retrieve the hostname part from a url prefixed by http://
        def getHostname(url: str) -> str:
            end_idx = 7
            while end_idx < len(url) and url[end_idx] != '/':
                end_idx += 1
            
            return url[7:end_idx]

        visited = set()
        res = []

        def dfs(url: str, hostname: str) -> None:
            nonlocal visited
            res.append(url)
            visited.add(url)

            for next_url in htmlParser.getUrls(url):
                if next_url in visited or getHostname(next_url) != hostname:
                    continue
                dfs(next_url, hostname)

            return

        dfs(startUrl, getHostname(startUrl))
        return res
