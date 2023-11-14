/* 
 * Node is defined as :
 *  typedef struct node {
 *     int val;
 *     struct node* right;
 *     int ht;
 *  } node; 
 */
int height(node* root) {
     if (root) {
          return root->ht;
     }
     return -1;
}

void updateHeight(node* root) {
     root->ht = 1 + max(height(root->left), height(root->right));
}

void rotateRight(node* &root) {
     node* temp = root->left;

     root->left = temp->right;
     temp->right = root;

     updateHeight(root);
     updateHeight(temp);

     root = temp;
}

void rotateLeft(node* &root) {
     node* temp = root->right;

     root->right = temp->left;
     temp->left = root;

     updateHeight(root);
     updateHeight(temp);

     root = temp;
}

int balanceFactor(node* root) {
     return height(root->left) - height(root->right);
}

node* insert(node* root, int val) {
     if (!root) {
          root = new node;
          root->val = val;
          root->left = nullptr;
          root->right = nullptr;
          root->ht = 0;
     } else if (val < root->val) {
          root->left = insert(root->left, val);
     } else {
          root->right = insert(root->right, val);
     }

     updateHeight(root);
     int bf = balanceFactor(root);

     if (bf > 1) {
          if (val < root->left->val) {
               rotateRight(root);
          } else {
               rotateLeft(root->left);
               rotateRight(root);
          }
     } else if (bf < -1) {
          if (val > root->right->val) {
               rotateLeft(root);
          } else {
               rotateRight(root->right);
               rotateLeft(root);
          }
     }
     return root;
}