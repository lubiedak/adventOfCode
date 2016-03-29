#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>

class Box{
public:
  Box(){}
  Box(std::string str){
    std::stringstream ss;
    std::string dim;
    ss << str;

    std::getline(ss, dim, 'x');
    l = std::stoi(dim);

    std::getline(ss, dim, 'x');
    w = std::stoi(dim);

    std::getline(ss, dim);
    h = std::stoi(dim);
  }

  void print(){
    std::cout<<l<<"\t"<<w<<"\t"<<h<<std::endl;
  }

private:
  int l;
  int w;
  int h;
  int min;
};


int main(){
  //Read file content
  std::ifstream file("input");
  std::vector<Box> boxes;
  std::string line;

  while(std::getline(file, line)){
    boxes.push_back(Box(line));
  }

  for(auto b : boxes)
    b.print();

  return 0;
}
