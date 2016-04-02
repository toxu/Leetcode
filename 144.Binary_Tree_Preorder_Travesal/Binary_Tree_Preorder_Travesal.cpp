/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    vector<int> preorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode *> s;
        TreeNode *node = root;
        while(node != NULL || !s.empty()){
            if(node != NULL){
                result.push_back(node);
                if(node->right != NULL)
                    s.push(node->right);
            }
            else{
                TreeNode *tmp = s.top();
                s.pop();
                node = tmp;
            }
        }        
        return result;
    }
};
