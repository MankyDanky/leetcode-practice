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
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int,int> leftChildren;
        unordered_map<int,int> rightChildren;

        unordered_set<int> children;
        unordered_set<int> nodes;

        for (vector<int>& d : descriptions) {
            int a = d[0], b = d[1], c = d[2];
            nodes.insert(a);
            nodes.insert(b);
            children.insert(b);
            if (c) {
                leftChildren[a] = b;
            } else {
                rightChildren[a] = b;
            }
        }

        function<void(TreeNode*)> dfs =  [&](TreeNode* node) {
            if (leftChildren.find(node->val) != leftChildren.end()) {
                TreeNode* left = new TreeNode();
                left->val = leftChildren[node->val];
                node->left = left;
                dfs(left);
            }

            if (rightChildren.find(node->val) != rightChildren.end()) {
                TreeNode* right = new TreeNode();
                right->val = rightChildren[node->val];
                node->right = right;
                dfs(right);
            }

            return;
        };

        TreeNode* node = new TreeNode();

        for (int a : nodes) {
            if (!children.contains(a)) {
                node->val = a;
                dfs(node);
                return node;
            }
        }
        return node;
    }
};
