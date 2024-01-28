1448. Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

#solution

As with binary trees always call it recursively,
Maybe one thing to notice is that usually adding arguments to the function is better rather than using a global variable. 