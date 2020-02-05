#include<stdio.h>
#include<sstream>
#include<iostream>
#include<string>

using namespace std;

int main()
{
    string str;
    string str1,str2;
    cout<<"enter string:";
    getline(cin,str);
    cout<<str<<endl;

    stringstream ss(str);

    for(int i = str.length()-1;i<str.length();i-- )
    {
        str1+=str[i];
    }

    cout<<"reverse::"<<str1<<endl;

    string ss1 = "Sivakumari";
    for(int i = 0,j= ss1.length()-1 ;i<ss1.length();i++,j--)
    {
        char s = ss1[i];
        ss1[i]= ss1[j];
        ss1[j] = ss1[i];
    }
    cout<<"ss1:"<<ss1<<endl;
    while(getline(ss,str2,' '))
        cout<<"word:"<<str2<<endl;
    return 0;
}
