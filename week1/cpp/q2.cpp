#include <iostream>
#include <math.h>

void solve() {
  int weight = 0;
  float height = 0;

  std::cout << "What's your weight (in kg)? ";
  std::cin >> weight;
  
  std::cout << "What's your height (in m)? ";
  std::cin >> height;

  float bmi = weight/pow(height, 2);
  std::cout << bmi << std::endl;

  return;
}

int main() {
  solve();
  return 0;
}
