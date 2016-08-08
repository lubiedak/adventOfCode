#include<string>

using namespace std;

string lookAndSay(string word) {
	int n = 1;
	char oldC = word.charAt(0);
	String newWord = "";
	int i = 1;
	std::string::iterator it=str.begin();
	
	for ( std::string::iterator it=str.begin(); it!=str.end(); ++it){
		
	}
		for (; i < word.length(); ++i) {
			if (oldC != word.charAt(i)) {
				newWord = newWord + n + oldC;
				n = 0;
			}
			oldC = word.charAt(i);
			n++;
		}
		newWord = newWord + n + oldC;
		return newWord;
	}

public static void main(String[] args) {
	// TODO Auto-generated method stub
	String word = "1113222113";
	for (int i = 0; i < 50; ++i) {
		word = lookAndSay(word);
		System.out.println("I: " + i + ", length: " + word.length());
	}

}