// OptimalRecipies.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <vector>
#include <iostream>

using namespace std;

enum {
	c, d, f, t, cal
};

int sprinkles[] = { 2, 0, -2, 0, 3 };
int butterScotch[] = { 0, 5, -3, 0, 3 };
int chocolate[] = { 0, 0,  5,-1, 8 };
int candy[] = { 0,-1 , 0, 5, 8 };

class Proportions {
public:
	Proportions(int size, int range) {
		this->size = size;
		this->range = range;
		p = vector<int>(size, 1);
	}

	void next() {
		++p[0];
		check = 0;
		while (check < size - 1) {
			if (p[check] == range) {
				++p[check + 1];
				p[check] = 0;
				check++;
			}
			else {
				break;
			}
		}
		
	}
	bool isMax() {
		int sum = 0;
		for (auto i : p) {
			sum += i;
		}
		return sum >size*range;
	}

	bool sumsToRange() {
		int sum = 0;
		for (auto i : p) {
			sum += i;
		}
		return sprinkles[4] * p[0] + butterScotch[4] * p[1] + chocolate[4] * p[2] + candy[4] * p[3] == 500 && sum == range;
	}

	void print() {
		for (auto i : p)
		{
			cout << i << "  ";
		}
		cout << endl;
	}

	vector<int> p;
private:

	int check;
	int size;
	int range;
};

int main()
{


	int bestProperty=1;
	int property = 1;

	int numbers = 4;
	int size = 100;
	Proportions p(4, 100);

	int i = 0;
	while (!p.isMax()) {
		while (!p.sumsToRange()) {
			p.next();
		}
		property = 1;
		for (int i = 0; i < numbers; ++i) {
			int pi = sprinkles[i] * p.p[0] + butterScotch[i] * p.p[1] + chocolate[i] * p.p[2] + candy[i] * p.p[3];
			if (pi > 0)
				property *= pi;
			else {
				property = 0;
				break;
			}
		}
		if (property > bestProperty) {
			bestProperty = property;
			cout << bestProperty<<"\t";
			p.print();
		}
		p.next();
		i++;
	}
	int a;
	cin >> a;
	return 0;
}

