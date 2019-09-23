// Find the Town Judge
// 42.32% time, 50.00% space
// Accepted

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int findJudge(int N, vector<vector<int> >& trust) {
        int *be_trusted = new int[N+1];
        bool *trusting = new bool[N+1];
        for(int i=1; i<=N; i++) {  // initialization
            be_trusted[i] = 0;
            trusting[i] = false;
        }

        for(auto iter:trust) {
            be_trusted[iter[1]] += 1;
            trusting[iter[0]] = true;
        }
        
        int judge;
        int possible_judge = 0;
        for(int i=1; i<=N; i++) {
            if(be_trusted[i] == N-1) {
                possible_judge++;
                judge = i;
            }
        }
        
        if (possible_judge != 1 || trusting[judge])
            return -1;

        return judge;
    }        
};

int main() {
    Solution test;
    // Example 1
    // vector<vector<int> > trust = {{1,2}};
    // int N = 2;
    // Example 2
    // vector<vector<int> > trust = {{1,3}, {2,3}};
    // int N = 3;
    // Example 3
    vector<vector<int> > trust = {{1,3}, {2,3}, {3,1}};
    int N = 3;
    // Example 4
    // vector<vector<int> > trust = {{1,2}, {2,3}};
    // int N = -1;
    // Example 5
    // vector<vector<int> > trust = {{1,3}, {1,4}, {2,3}, {2,4}, {4,3}};
    // int N = 3;
    int res = test.findJudge(N, trust);
    cout << res << endl;

    return 0;
}
