#include <iostream>
#include <thread>

int
main(int argc, char **argv)
{

  std::thread t1([] {
      std::cout << "Hello, World - CPP" << std::endl;
    });
  t1.join();
  return 0;
}
