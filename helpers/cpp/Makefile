CC		= g++
CCOPT		= -O3 -c

nimseq.exe : main.o Compute.o Set.o
	$(CC) -O3 main.o Compute.o Set.o -o nimseq.exe

main.o : main.cpp Compute.o Set.o
	$(CC) $(CCOPT) main.cpp -o main.o -Wall

Compute.o : Compute.cpp Set.o
	$(CC) $(CCOPT) Compute.cpp -o Compute.o -Wall

Set.o : Set.cpp 
	$(CC) $(CCOPT) Set.cpp -o Set.o -Wall
