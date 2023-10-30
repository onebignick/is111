#include <iostream>
#include <fstream>
#include <string>

void sum_up(std::string filestring)
{
  std::fstream infile;
  infile.open(filestring,std::ios::in);

  float sum = 0;
  std::string line;

  while (std::getline(infile,line))
  {
    sum += atof(line.c_str());
  }

  std::cout << sum << std::endl;
}

int main()
{
  sum_up("../src/q1-1.txt");
  sum_up("../src/q1-2.txt");
}
