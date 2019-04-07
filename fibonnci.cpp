#include<iostream>
using namespace std;

int main()
{
	int n,a=0,b=1,c;
	cout<<"Enter Range:";
	cin>>n;
	cout<<a<<"\n";
	cout<<b<<"\n";
	for(int j=2;j<=n;j++)
	{
		c=a+b;
		a=b;
		b=c;
		cout<<c<<"\n";
	}
	return 0;
}
