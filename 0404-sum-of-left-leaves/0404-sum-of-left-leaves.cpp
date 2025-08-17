class Solution {
public:
    int ans=0;
    void leftLeaf(TreeNode* root)
    {
        if(root==NULL) return;
        if(root->left)
        {
            if(root->left->left==NULL && root->left->right==NULL)  ans+= root->left->val;
        }
        leftLeaf(root->left);
        leftLeaf(root->right);

    }
    int sumOfLeftLeaves(TreeNode* root) {
        leftLeaf(root);
        return ans;
    }
};