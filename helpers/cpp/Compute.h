#ifndef DEF_COMPUTE
#define DEF_COMPUTE

#include <iostream>
#include <string>
#include <vector>
#include "Set.h"

class Compute
{
 public:
 Compute(std::vector<int> set);

 void forward();
 void allForward(int maxElem);
 void displayInTerminal();
 void displayInFile(std::string output);

 private:
 std::vector<int> m_set; // initial set, to let in an increasing order, with only positive numbers
 std::vector<int> m_nimseq; // sequence obtained
 int m_site; // the current site of the sequence we want to know

 int m_biggestNumberSeen; // the biggest number seen in the sequence until now
 int m_percent; // from 0 to 100, to know the progress of the computation
};

#endif
