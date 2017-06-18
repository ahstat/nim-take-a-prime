#include "Compute.h"
using namespace std;

Compute::Compute(std::vector<int> set) : m_set(set)
{
 m_nimseq.resize(0);
 m_site = 0;
 m_biggestNumberSeen=0;
 m_percent=0;
}

void Compute::allForward(int maxElem)
{
 if(maxElem == 0)
 {
  maxElem = m_set.back();
 }

 //Note: for m_site > maxElem, we don't know the elements of the sequence
 while(m_site < maxElem)
 {
  double percent((double) m_site / (double) m_set.back());
  if(100*percent>m_percent)
  {
   cout << m_percent << "%" << endl;
   m_percent+=1;
  }
  forward();
 }
}

void Compute::forward()
{
 // if(m_site > m_set.back())
 // {
 //  cout << "ERROR: increase the length of the set file." << endl;
 // }

 // nextOne represents the possible values for the next term of the sequence
 // nextOne[l]=1 means that the next term could be 1.
 vector<bool> nextOne(m_biggestNumberSeen+1, 1);

 for(unsigned int i(0); i<m_set.size(); i++)
 {
  if(m_site-m_set[i] >= 0)
  {
   int notIt(m_nimseq[m_site-m_set[i]]);
   if(notIt > m_biggestNumberSeen)
   {
    cout << "ERROR" << endl;
   }
   else
   {
    nextOne[notIt]=0;
   }
  }
  else //the next one is negative, so the next ones too, and we can break the computation here
  {
   break;
  }
 }

 /*
 for(unsigned int i(0); i<nextOne.size(); i++)
 {
  cout << i << " ";
 }
 cout << endl;
 for(unsigned int i(0); i<nextOne.size(); i++)
 {
  cout << nextOne[i] << " ";
 }
 cout << endl << endl;
 */

 // taking the lowest index l with nextOne[l]=1 for the term m_nimseq of the current site
 // This loop may be improved to increase computational efficiency
 // (remove break, remove push_back)
 for(unsigned int i(0); i<nextOne.size(); i++)
 {
  if(nextOne[i]==1)
  {
   m_nimseq.push_back(i);
   break;
  }
  else if(i==nextOne.size()-1)
  {
   cout << "a new number for site " << m_site << ": " << i+1 << endl;
   m_nimseq.push_back(i+1);
   m_biggestNumberSeen+=1;
  }
 }

 m_site+=1;
}

void Compute::displayInTerminal()
{
 cout << "Displaying the whole sequence." << endl;
 for(unsigned int i(0); i<m_nimseq.size(); i++)
 {
  cout << m_nimseq[i] << " ";
 }
 cout << endl << endl;
}

void Compute::displayInFile(string output)
{
 ofstream outFlow(output.c_str());

 for(unsigned int i(0); i<m_nimseq.size(); i++)
 {
  outFlow << m_nimseq[i] << "\n";
 }
}
