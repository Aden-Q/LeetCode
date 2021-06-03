// Binary Tree Zigzag Level Order Traversal
// 62.49% time and 46.53% space AC

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
		vector<vector<int>> res;
		vector<int> temp;	// store one level
		stack<TreeNode*> s0;
		stack<TreeNode*> s1;
		s0.push(root);

        if (root == nullptr) 
        	return res;

        for (int i=1; i<=findHeight(root); i++) {
        	temp.clear();
            // number of levels
            if (i%2 == 1) {
            	int sz = s0.size();
		        for (int j=0; j<sz; j++) {
		        	TreeNode* cur = s0.top();
		        	temp.push_back(cur->val);
		        	s0.pop();
		        	if (cur->left != nullptr)
		        		s1.push(cur->left);
		        	if (cur->right != nullptr)
		        		s1.push(cur->right);
		        }
            } else {
            	int sz = s1.size();
            	for (int j=0; j<sz; j++) {
		        	TreeNode* cur = s1.top();
		        	temp.push_back(cur->val);
		        	s1.pop();
		        	if (cur->right != nullptr)
		        		s0.push(cur->right);
		        	if (cur->left != nullptr)
		        		s0.push(cur->left);
            	}
            }
            res.push_back(temp);
        }

        return res;
    }

    // Get the height of the tree
    int findHeight(TreeNode* root) {
    	if (root == nullptr)
    		return 0;
    	return max(findHeight(root->left), findHeight(root->right)) + 1;
    }
};
