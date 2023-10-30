#include <fstream>
#include <iostream>
#include <string>

void create_number_file(std::string output_file_name, int n)
{
  std::ofstream outfile{output_file_name};

  if(!outfile)
  {
    std::cerr << "Error: could not open file" << std::endl;
    return;
  }

  for (int i=0;i<=n;i=i+2)
  {
    outfile << i << '\n';
  }
  return;
}

int main()
{
  create_number_file("q1-output.txt",10);
}
