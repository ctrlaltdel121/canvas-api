// my first program in C++
#include <iostream>

int main(int argc, char *argv[])
{

  if (argc != 2) {
    std::cout << "Invalid input" << std::endl;
    return 1;
  }
  std::cout << "Hello " << argv[1] << "!" << std::endl;
  // std::cout << argv[1];
  // std::cout << "!"
  // std::cout << std::endl;
}