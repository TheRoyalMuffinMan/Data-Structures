/*
 * File Name: treeset_funcs.c
 * The following C file consist of functions that used within the treeset_main program.
 * The functions here operate on a binary search tree with unique strings.
 * @author Andy
 * @since 11/15/2021
 */

#include "treeset.h"

/*
 * The treeset_init() function takes a tree as parameters and initializes its fields 
 * of that tree's struct.
 * @param tree that will have its fields initialized
 */
void treeset_init(treeset_t *tree) {
	tree->root = NULL;
	tree->size = 0;
}

/*
 * The treeset_insert() function takes a tree and a name as parameters. 
 * The function then attempts to add the name to the binary search tree.
 * It first determines if the root is null, if it is the root is initialized and its
 * data is set to the name. If the tree is defined and the root isn't null,
 * the function iteratively traverses the tree till it finds the position of where the 
 * node should be added at. If there is a node already there with the same data as the 
 * passed name, the function returns 0 and nothing is done (no duplicates allowed).
 * If there is not a node present there, a node is defined with the passed name as the data
 * of that node, the count of the nodes in the tree increments, and the function returns 1. This is done
 * in O(log n) time for a balanced BST and O(n) time for a unbalanced BST.
 * @param tree which will either have a new node added to it or not
 * @param character array that represents that string name to be added to the BST
 * @return 1 on successful addition of the new node, else 0 if the node is already present
 */
int treeset_insert(treeset_t *tree, char name[]) {
	// Base Case: Empty Tree (no root)
	if (tree->root == NULL) {
		tree->root = malloc(sizeof(tsnode_t));
		strcpy(tree->root->name, name);
		tree->root->left = NULL;
		tree->root->right = NULL;
		tree->size = 1;
		return 1;
	} else {
		// Define a parent which will have the new name added onto
		tsnode_t *curr = tree->root, *parent = tree->root;
		while (curr != NULL) {
			parent = curr;
			// curr->name < name, then go right
			if (strcmp(curr->name, name) < 0) {
				curr = curr->right;
			// curr->name > name, then go left
			} else if (strcmp(curr->name, name) > 0) {
				curr = curr->left;
			// curr->name = name, exit the function
			} else {
				return 0;
			}
		}
		// parent->name < name, add to the right child
		if (strcmp(parent->name, name) < 0) {
			parent->right = malloc(sizeof(tsnode_t));
			strcpy(parent->right->name, name);
			parent->right->left = NULL;
			parent->right->right = NULL;
		// parent->name > name, add to the left child
		} else {
			parent->left = malloc(sizeof(tsnode_t));
			strcpy(parent->left->name, name);
			parent->left->left = NULL;
			parent->left->right = NULL;
		}
		tree->size++;
		return 1;
	}
}

/*
 * The treeset_find() function takes a tree and a name as parameters. These parameters 
 * are then used to search through the tree till the node with the same name is located. 
 * If the target name that is being searched for is located it, it returns 1 else the 
 * function returns 0.  This is done in O(log n) time if the tree is balanced, if the 
 * tree isn't balanced, its done in O(n) time.
 * @param pointer to a struct type treeset_t that represents the tree
 * @param character array that represents the string target being searched for
 */
int treeset_find(treeset_t *tree, char name[]) {
	// Base Case: Empty Tree
	if (tree->root == NULL) {
		return 0;
	} else {
		tsnode_t *curr = tree->root;
		while (curr != NULL) {
			// curr->name < name, then go right
			if (strcmp(curr->name, name) < 0) {
				curr = curr->right;
			// curr->name > name, then go left
			} else if (strcmp(curr->name, name) > 0) {
				curr = curr->left;
			// curr->name = name, node found, exit the function
			} else {
			
				return 1;
			}
		}
		return 0;
	}
}

/*
 * The treeset_clear() function takes a tree as parameters and then proceeds to 
 * remove all the existing nodes in the tree by using a recursive helper function.
 * Then resets all the root and size fields of the tree.
 * @param pointer to a struct of type treeset_t that represents a tree that will be cleared
 */
void treeset_clear(treeset_t *tree) {
	// Base Case: Empty tree
	if (tree->root == NULL) {
		return;
	} else {
		tsnode_remove_all(tree->root);
		tree->root = NULL;
		tree->size = 0;
	}
}

/*
 * The tsnode_remove_all() function takes a node as parameters and recursively 
 * traverses the left and root subtrees of the respective starting node (root). 
 * This is done using a post-order traversal, Go Left, Go Right, Visit Node.
 * @param current node that it is traversing from or freeing (if left and right = null)
 */
void tsnode_remove_all(tsnode_t *curr) {
	if (curr->left != NULL) {
		tsnode_remove_all(curr->left);
	}
	if (curr->right != NULL) {
		tsnode_remove_all(curr->right);
	}
	free(curr);
}

/*
 * The treeset_print_revorder() function takes a tree as parameters and proceeds
 * to print out the tree in reverse order using a recursive helper function.
 * @param tree that is printed out in reverse order
 */
void treeset_print_revorder(treeset_t *tree) {
	// Base Case: Empty tree
	if (tree->root == NULL) {
		return;
	} else {
		tsnode_print_revorder(tree->root, 0);
	}
}

/*
 * The tsnode_print_revorder() takes a node and indentation number as parameters
 * and uses them to format the reverse ordered output of the tree. The indentaton parameter
 * indicates the number of 2 spaces difference from the root, this is counted up recursively
 * as we dive down the tree using a backwards inorder traversal: Go Right, Visit Node, Go Left.
 * @param current node being traversed down, (if right has been visited and can't be visited anymore,
 * the node is printed), then we go left
 * @param count of the current indentation number that correlates the specific depth of the node in the tree
 */
void tsnode_print_revorder(tsnode_t *curr, int indent) {
	if (curr->right != NULL) {
		tsnode_print_revorder(curr->right, indent + 1);
	}
	for (int i = 0; i < indent; i++) {
		printf("  ");
	}
	printf("%s\n", curr->name);
	if (curr->left != NULL) {
		tsnode_print_revorder(curr->left, indent + 1);
	}
}

/*
 * The treeset_print_preorder() takes a tree as parameters and uses a recursive helper function
 * to print out the nodes in preorder. Preorder is defined as: Visit Node, Go Left, then Go Right.
 * Note: The recursive helper function is a helper for another function, so instead of the tree's root being 
 * passed through only, other special parameters must be passed to indicate that the tree should be ONLY printed
 * in preorder.
 * @param the tree that is to be printed out in preorder
 */
void treeset_print_preorder(treeset_t *tree) {
    // Base Case: Empty tree
	if (tree->root == NULL) {
		return;
	} else {
		tsnode_write_preorder(tree->root, NULL, 0);
	}
}

/*
 * The treeset_save() function takes a tree as parameters and writes it to a file. This
 * is done recursively using a helper function known as tsnode_write_preorder() in preorder. NOTE: 
 * special parameters are given so that it actually writes the tree to file versus printing it.
 * @param tree that will be written to a file
 * @param name of the file that will be opened and then closed
 */
void treeset_save(treeset_t *tree, char *fname) {
	FILE *pFile = fopen(fname, "w");
	// Base Case: Empty tree or File couldn't be opened
	if (pFile == NULL || tree->root == NULL) {
		return;
	} else {
		tsnode_write_preorder(tree->root, pFile, 0);
		fclose(pFile);
	}
}

/*
 * The tsnode_write_preorder() function takes a node, a file, and the current node's depth
 * as parameters and either prints or writes the node and its subtrees. The nodes are 
 * printed/written using a preorder traversal, and every subtree is indented by (2 spaces) * depth.
 * @param current node that is being traversaled down
 * @param file that the node will be written to in preorder
 * @param depth of the current root (with respect to the root)
 */
void tsnode_write_preorder(tsnode_t *curr, FILE *out, int depth) {
	if (out == NULL) { 						// Printing the tree
		for (int i = 0; i < depth; i++) {
			printf("  ");
		}
		printf("%s\n", curr->name);
		if (curr->left != NULL) {
			tsnode_write_preorder(curr->left, NULL, depth + 1);
		}
		if (curr->right != NULL) {
			tsnode_write_preorder(curr->right, NULL, depth + 1);
		}
	} else { 								// Writing the tree to a file
		for (int i = 0; i < depth; i++) {
			fprintf(out, "  ");
		}
		fprintf(out, "%s\n", curr->name);
		if (curr->left != NULL) {
			tsnode_write_preorder(curr->left, out, depth + 1);
		}
		if (curr->right != NULL) {
			tsnode_write_preorder(curr->right, out, depth + 1);
		}
	}
}

/*
 * The treeset_load() function takes a tree as parameters and loads it from the
 * given file. The tree is first cleared and then treeset_insert() is repeatedly
 * called till all the nodes have been written. If the file couldn't open, 0 is
 * returned else 1 is returned.
 * @param tree that will be loaded from the file
 * @param file name of the file that the tree will be loaded from
 * @return 0 if the file can't be loaded, else 1
 */
int treeset_load(treeset_t *tree, char *fname ) {
	FILE *pFile = fopen(fname, "r");
	// Base Case: File can't be opened
	if (pFile == NULL) {
		return 0;
	} else {
		treeset_clear(tree);
		char name[128];
		while(fscanf(pFile, "%s", name) != EOF) {
			treeset_insert(tree, name);
		}
		fclose(pFile);
		return 1;
	}
}
