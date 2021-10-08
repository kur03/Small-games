all: compile execute clear

compile: puissance4.o
	gcc -Wall puissance4.o -o P4

puissance4.o: puissance4.c
	gcc -Wall puissance4.c -c

execute: P4
	./P4

clear:
	rm *.o P4