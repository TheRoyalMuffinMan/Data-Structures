// Header file for the BST
#ifndef TREE_H
#define TREE_H 1

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

// Nodes that go into the tree
typedef struct tsnode {
  char name[128];               // tsnode data
  struct tsnode *left;          // left branch,  NULL if not present
  struct tsnode *right;         // right branch, NULL if not present
} tsnode_t;

// Type of tree itself
typedef struct {
  tsnode_t *root;
  int size;                     // number of tsnodes in tree
} treeset_t;

// tree function prototypes
void treeset_init(treeset_t *tree);
int treeset_insert(treeset_t *tree, char name[]);
int treeset_find(treeset_t *tree, char name[]);
void treeset_clear(treeset_t *tree);
void treeset_print_revorder(treeset_t *tree);
void treeset_print_preorder(treeset_t *tree);
void treeset_save(treeset_t *tree, char *fname);
int treeset_load(treeset_t *tree, char *fname);

// tsnode functions prototypes
tsnode_t *tsnode_insert(tsnode_t *cur, char name[]);
int tsnode_find(tsnode_t *cur, char name[]);
void tsnode_remove_all(tsnode_t *cur);
void tsnode_print_revorder(tsnode_t *cur, int indent);
void tsnode_write_preorder(tsnode_t *cur, FILE *out, int depth);

#endif
