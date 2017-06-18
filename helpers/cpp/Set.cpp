#include "Set.h"
using namespace std;

std::vector<int> Set::set()
{
 vector<int> output(58);
 output[0]=2;
 output[1]=3;
 output[2]=5;
 output[3]=7;
 output[4]=11;
 output[5]=13;
 output[6]=17;
 output[7]=19;
 output[8]=23;
 output[9]=29;
 output[10]=31;
 output[11]=37;
 output[12]=41;
 output[13]=43;
 output[14]=47;
 output[15]=53;
 output[16]=59;
 output[17]=61;
 output[18]=67;
 output[19]=71;
 output[20]=73;
 output[21]=79;
 output[22]=83;
 output[23]=89;
 output[24]=97;
 output[25]=101;
 output[26]=103;
 output[27]=107;
 output[28]=109;
 output[29]=113;
 output[30]=127;
 output[31]=131;
 output[32]=137;
 output[33]=139;
 output[34]=149;
 output[35]=151;
 output[36]=157;
 output[37]=163;
 output[38]=167;
 output[39]=173;
 output[40]=179;
 output[41]=181;
 output[42]=191;
 output[43]=193;
 output[44]=197;
 output[45]=199;
 output[46]=211;
 output[47]=223;
 output[48]=227;
 output[49]=229;
 output[50]=233;
 output[51]=239;
 output[52]=241;
 output[53]=251;
 output[54]=257;
 output[55]=263;
 output[56]=269;
 output[57]=271;
 return output;
}

vector<int> Set::setFile(string fileName)
{
 vector<int> output;
 ifstream flow(fileName.c_str());
 if(flow)
 {
 }
 else
 {
  cout << "ERROR Set: impossible to read-open the file." << endl;
 }
 double nextNumber;
 while(flow >> nextNumber) // while we don't reach the end of the file, we read it
 {
  output.push_back(nextNumber);
 }
 return output;
}

void Set::display(std::vector<int> sequence)
{
 for(unsigned int i(0); i<sequence.size(); i++)
 {
  cout << sequence[i] << " ";
 }
 cout << endl;
}
