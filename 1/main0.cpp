#include <iostream>
#include <string>
#include <vector>
#include <fstream>

int main(){
  //Read file content
  std::ifstream file("input");
  std::vector<std::string> input;
  std::string line;

  while(std::getline(file, line)){
    input.push_back(line);
  }

  return 0;
}
