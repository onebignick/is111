#include <iostream>
#include <vector>

void solve() 
{
  int num=0;
  int odd=0;
  int even=0;

  for(int i=0;i<4;i++)
  {

    std::cin >> num;

    if(num&1)
    {
      odd++;
    }
    else
    {
      even++;
    }

  }

  std::cout << "Odd percentage " << (float)odd/4 * 100 << "%" << '\n';
  std::cout << "Even percentage " << (float)even/4 * 100 << "%" << '\n';
  return;
}

int main() {
  solve();
  return 0;
}
