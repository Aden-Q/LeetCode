// Valid Perfect Square
// 53.63% time, 76.19% space
// Accepted

#include <iostream>
#include <math.h>

using namespace std;


class Solution {
public:
    // This helper function evaluate whether the square of the average of low and high equals the target 
    bool evaluate(int low, int high, int target) {
        // base case
        int median = (low+high) / 2;
        if (low == high || median == low || median == high)    return false;
        if (median*median == target)    return true;
        else if (target > median*median)    return evaluate(median, high, target);
        else    return evaluate(low, median, target);
    }

    bool isPerfectSquare(int num) {
        if (num < 0)
            return false;
        else if (num == num*num)
            return true;

        return evaluate(0, num, num);
    }
};


int main() {
    Solution test;
    int res1 = test.isPerfectSquare(16);
    int res2 = test.isPerfectSquare(14);
    cout << res1 << endl;
    cout << res2 << endl;

    return 0;
}
