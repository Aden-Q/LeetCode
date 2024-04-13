// Word Ladder
// 25.66% time, 97.73% space
// Accepted

#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        vector<string>::iterator it;
        // Extrema case
        for (it=wordList.begin(); it!=wordList.end(); it++)
            if (*it==endWord)
                break;
        if (it==wordList.end()) // the case that the wordList doesn't contain the endWord
            return 0;
        
        // Based on the requirement which is "shortest". BFS seems to be a good choice
        queue<string> q;
        unordered_set<string> hashset(wordList.begin(), wordList.end());
        int step = 0;
        int listSize = wordList.size();
        q.push(beginWord);
        while (!q.empty()) {
            step += 1;
            if (step > listSize+1)
                return 0;
            int size = q.size();
            for (int i=0; i<size; i++) {
                string s = q.front();
                if (s == endWord)
                    return step;
                // on this step, we need to boost enqueue from O(n^2) to O(n)
                for (unordered_set<string>::iterator iter=hashset.begin(); iter!=hashset.end();) {
                    if (stringCompare(*iter, s)) {
                        q.push(*iter);
                        hashset.erase(iter++);
                    }
                    else
                        ++iter;
                }
                q.pop();
            }
        }
        
        return 0;
    }

    bool stringCompare(string s1, string s2) {
        // return true if these is only one different character
        int count = 0;
        for (int i=0; i<s1.length(); i++)
            if (s1[i] != s2[i])
                count++;
        
        return count == 1;
    }
};


int main() {
    Solution test;
    string beginWord = "hog";
    string endWord = "cog";
    vector<string> wordList = {"cog"};
    // vector<string> wordList = {"hot", "dot", "dog", "lot", "log", "cog"};
    // vector<string> wordList = {"hot", "dot", "dog", "lot", "log"};
    // vector<string> wordList = {"a", "b", "c"};
    int res = test.ladderLength(beginWord, endWord, wordList);
    cout << res << endl;

    return 0;
}

