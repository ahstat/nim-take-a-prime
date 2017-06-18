#include <iostream>
#include <vector>
#include "Set.h"
#include "Compute.h"

using namespace std;

// A014589 Nim function for Take-a-Prime (or Subtract-a-Prime) Game. 
// http://oeis.org/A014589

int main(int argc, const char * argv[]) 
{
  for(int i = 0; i < argc; i++)
  {
    printf("Argument %i = %s\n", i, argv[i]);
  }

  string filename = argv[1];
  string outname = argv[2];
  int maxElem = 0; // Max element for which we can compute the Nim sequence
  // Example: If we take the primes smaller than 1000, the last element is 997.
  // But it is safe to compute the Nim sequence until 1000
  if(argc == 4)
  {
    maxElem = strtol(argv[3], NULL, 10);
  }
 
 cout << "Loading set file." << endl;
 vector<int> set(Set::setFile(filename)); // Load a set from a file
 //Set::display(set);
 cout << "File loaded, of length " << set.size() << "." << endl;
 cout << "Object creation." << endl;
 Compute compute(set);
 cout << "Computing the sequence." << endl;
 compute.allForward(maxElem);
 cout << "End of the computation." << endl;
 compute.displayInFile(outname);
 return 0;
}
