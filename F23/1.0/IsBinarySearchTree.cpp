/* 
 * Hidden stub code will pass a root argument to the function below.
 * Complete the function to solve the challenge. 
 * Hint: you may want to write one or more helper functions.
 * 
 * The Node struct is defined as follows:
 *    struct Node {
 *         int data;
 *       Node* left;
 *       Node* right;
 *  }
 */
bool checkBST(Node* root) {
     return checkBST_Helper(root, nullptr, nullptr);
}

bool checkBST_Helper(Node* node, Node* left, Node* right) {
     if (!node) {
          return true;
     }

     if ((left && node->data <= left->data) || (right && node->data >= right->data)) {
          return false;
     }

     return checkBST_Helper(node->left, left, node) && checkBST_Helper(node->right, node, right);
}