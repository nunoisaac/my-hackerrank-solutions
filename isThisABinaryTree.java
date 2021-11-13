public class isThisABinaryTree {
    public static void main(String[] args){
    /*
    HackerRank Challenge: Is this a binary tree?
    Practice > Data Structures > Trees > Is This a Binary Search Tree?

    For the purposes of this challenge, we define a binary tree to be a binary search tree with the following ordering
    requirements:

     - The data value of every node in a node's left subtree is less than the data value of that node.
     - The data value of every node in a node's right subtree is greater than the data value of that node.
    Given the root node of a binary tree, can you determine if it's also a binary search tree?

    Complete the function in your editor below, which has  parameter: a pointer to the root of a binary tree. It must
    return a boolean denoting whether the binary tree is a binary search tree. You may have to write one or more
    helper functions to complete this challenge.
    */

    }
    static boolean checkBST(Node root) {
        if(root != null){
            return inOrderTrav(root, Integer.MIN_VALUE, Integer.MAX_VALUE);
        }
        return false;
    }
    /*
    R represents the value that all node values in the right subtree must be larger than.
    L represents the value that all node values in the left subtree must be smaller than.
    L and R form a range where the current node value must be greater than R but less than L to be a valid binary tree.
    R < curr < L
     */
     static boolean inOrderTrav(Node root, int R, int L){
        if(root != null){
            if(inOrderTrav(root.left, R, root.data)){
                if(R >= root.data || root.data >= L)
                    return false;
                return inOrderTrav(root.right, root.data, L);
            }
            return false;
        }
        return true;
    }
}
