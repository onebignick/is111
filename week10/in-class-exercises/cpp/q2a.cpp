#include <fstream>
#include <iostream>
#include <string>
#include <vector>

void get_books_cheaper_than ()
{
  std::ifstream infile{"../src/books-1.txt",std::ios::out};
  while (infile)
  {
    std::string strInput;
    std::vector<std::string>line(3);
    for(std::string temp; std::getline(infile,strInput,'\t');)
    {
      line.push_back(temp);
      std::cout<<temp<<'\n';
    }
  }
  return;
}

int main()
{
  get_books_cheaper_than();
}
