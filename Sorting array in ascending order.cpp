#include<iostream>
using namespace std ;

int main()
{
	int size,i,j,temp;
	int arr[100];
	cout<<"Size of array";
	cin>>size;
	cout<<"Enter array";
	for(i=0 ;i<size;i++)
	{
		cin>>arr[i];
		cout<<arr[i];
	}
	for(i=0;i<size;i++)
	{
		for(j=i+1;j<size;j++)
		{
			if(arr[j]<arr[i])
			{
				temp=arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
				
			}
		}
	}
	cout<<"element are sorted";
	for(i=0;i<size;i++)
	{
		cout<<arr[i]<<endl;
		
	}
	return 0;
}
	

