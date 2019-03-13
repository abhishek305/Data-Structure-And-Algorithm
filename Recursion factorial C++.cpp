#include<iostream>
using namespace std;

int fact(int n)
{
	
	if (n==0)
	return 1;
	else
	{
		return (n*fact(n-1));
	}
	
}
int main()
{
	int var,d;
	cin>>d;
	var=fact(d);
	cout<<var;
	return 0;
}
