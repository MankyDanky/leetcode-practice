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
private:
    int res = 0;
public:
    pair<int,int> checkNode(TreeNode* node) {
        if (node == nullptr) return {0,0};
        int nodes = 0;
        int sum = 0;
        
        pair<int,int> left = checkNode(node->left);
        pair<int,int> right = checkNode(node->right);

        nodes = left.first + right.first + 1;
        sum = left.second + right.second + node->val;

        if (sum/nodes == node->val) this->res += 1;

        return {nodes, sum};
    }

    int averageOfSubtree(TreeNode* root) {
        checkNode(root);
        return this->res;
    }
};
