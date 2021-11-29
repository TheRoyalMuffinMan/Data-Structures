/*
 * File Name: treeset_main.c
 * The following C file is the main function for the treeset package. Main will invoke
 * function calls from treeset_funcs.c that will depend on the input from the user.
 * @author Andrew Hoyle
 * @since 11/15/2021
 */
 
#include "treeset.h"

int main(int argc, char *argv[]) {
	treeset_t tree; treeset_init(&tree);      // setting up the tree on the stack and initializing its fields
	char cmd[128];                           
	int success, echo = 0;                    // echo - used for the test cases         
  	if (argc > 1 && strcmp("-echo", argv[1]) == 0) { 
    	echo = 1;
  	}
	
	printf("Treeset Main\n");
  	printf("Commands:\n");
  	printf("  print:          shows contents of the tree in reverse sorted order\n");
  	printf("  size:           prints the number of nodes currently in the tree\n");
  	printf("  clear:          eliminates all elements from the tree\n");
  	printf("  quit:           exit the program\n");
  	printf("  add <name>:     inserts the given string into the tree, duplicates ignored\n");
  	printf("  find <name>:    prints FOUND if the name is in the tree, NOT FOUND otherwise\n");
  	printf("  preorder:       prints contents of the tree in pre-order which is how it will be saved\n");
  	printf("  save <file>:    writes the contents of the tree in pre-order to the given file\n");
  	printf("  load <file>:    clears the current tree and loads the one in the given file\n");
  	
  	while (1) {
  		printf("TS#> ");
  		success = fscanf(stdin,"%s", cmd);    // read an option
    	if (success == EOF) {             	  // check for end of input
      		printf("\n");                 	
      		break;                        	
    	}
  		if (strcmp(cmd, "print") == 0) {
  			if (echo) {
  				puts("print");
  			}
  			treeset_print_revorder(&tree);
  		} else if (strcmp(cmd, "size") == 0) {
  			if (echo) {
  				puts("size");
  			}
  			printf("%d nodes\n", tree.size);
  		} else if (strcmp(cmd, "clear") == 0) {
  			treeset_clear(&tree);
  			if (echo) {
  				puts("clear");
  			}
  		} else if (strcmp(cmd, "quit") == 0) {
  			if (echo) {
  				puts("quit");
  			}
  			break;
  		} else if (strcmp(cmd, "add") == 0) {
  			fscanf(stdin, "%s", cmd);		  // read in a string to be added to the tree
  			if (echo) {
  				printf("add %s\n", cmd);
  			}
  			if (!treeset_insert(&tree, cmd)) {
  				puts("duplicate element ignored");
  			}
  		} else if (strcmp(cmd, "find") == 0) {
  			fscanf(stdin, "%s", cmd);         // read in a string to be searched for in the tree
  			if (echo) {
  				printf("find %s\n", cmd);
  			}
  			printf("%s\n", (treeset_find(&tree, cmd)) ? "FOUND" : "NOT FOUND"); 		
  		} else if (strcmp(cmd, "preorder") == 0) {
  			if (echo) {
  				puts("preorder");
  			}
  			treeset_print_preorder(&tree);
  		} else if (strcmp(cmd, "save") == 0) {
  			fscanf(stdin, "%s", cmd);         // read in a file name to which the tree will be saved to
  			treeset_save(&tree, cmd);
  			if (echo) {
  				printf("save %s\n", cmd);
  			}
  		} else if (strcmp(cmd, "load") == 0) {
  			fscanf(stdin, "%s", cmd);         // read in a file name that loads a tree from it
  			treeset_load(&tree, cmd);
  			if (echo) {
  				printf("load %s\n", cmd);
  			}
  		} else {
  			printf("UNKNOWN COMMAND: %s\n",cmd);
  		}
  	}
  	treeset_clear(&tree);                     // clear the tree before the function ends
  	return 0;
}
