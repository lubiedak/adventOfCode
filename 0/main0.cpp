#include <iostream>
#include <string>
#include <fstream>

int main(){
  //Read file content
  std::ifstream file("input");
  std::string input;
  std::getline(file, input);

  int level = 0;
  for(std::string::size_type i = 0; i < input.size(); ++i){
    if(input[i] == '(')
      ++level;
    if(input[i] == ')')
      --level;
    if(level==-1){
      std::cout<<i+1<<std::endl;
      break;
    }
  }
  return 0;
}
