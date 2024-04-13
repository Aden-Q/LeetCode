// Top K Frequent Elements
// 35.37% time, 96.77% space
// Accepted

#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;
typedef pair<int, int> P;

struct cmp {
    bool operator()(const P p1, const P p2) {
        return p1.second < p2.second;
    }
};


class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        unordered_map<int, int> hashmap;
        // count how many times each element appears
        for(int n:nums) {
            if(hashmap.count(n) <= 0)
                hashmap[n] = 1;
            else
                hashmap[n]++;
        }
        // construct the priority queue
        priority_queue<P, vector<P>, cmp> q;
        for(auto it=hashmap.begin(); it!=hashmap.end(); it++)
            q.push(make_pair(it->first, it->second));
        // dequeue top k elements
        for(int i=0; i<k; i++) {
            res.push_back(q.top().first);
            q.pop();
        }
        
        return res;
    }
};

int main() {
    Solution test;
    // Example 1
    // vector<int> nums = {1,1,1,2,2,3};
    // int k = 2;
    // Example 2
    vector<int> nums = {1};
    int k = 1;
    vector<int> res = test.topKFrequent(nums, k);
    for(auto it:res)
        cout << it << endl;

    return 0;
}
