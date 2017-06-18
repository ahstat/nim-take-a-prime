#ifndef DEF_SET
#define DEF_SET

#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <sstream>  
#include <utility>
#include <algorithm>

class Set
{
 public:
 static std::vector<int> set(); // default set (58 first prime numbers)
 static std::vector<int> setFile(std::string fileName); // load a set from a file
 static void display(std::vector<int> sequence);
 private:
};

#endif
