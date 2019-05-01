#include<iostream>
using namespace std;

int missno(int a[] , int n)
{
	int i,total,sum;
	total=(n+1)*(n+2)/2;
	for(i=0;i<n;i++)
	{
		total-=a[i];
	}
	return total;
}
int main()
{
	int a[]={1,2,3,4,6,7};
	int size = 6;
	int miss=missno(a,size);
	cout<<miss;
	return 0;
	
}
