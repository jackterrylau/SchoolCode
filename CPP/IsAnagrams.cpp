#include "stdafx.h"     // Visual Studio as IDE.
#include <iostream>
#include <string>

using namespace std;

int countString(const string& original)
{
     int count=0;
     
     for (int i = 0; i < original.length(); i++)
     {
         count += int(tolower(original[i])); // 把所有大寫字母轉小寫再加總.
     }
     return count;
}

bool isAnagram(const string& s1, const string& s2)
{
     string sorts;

     if (s1.length() == s2.length())
     {
         if (countString(s1) == countString(s2)) return true;
     }
     return false;
}

int main()
{

     string s1, s2;
     cout << "Enter a string s1: ";
     cin >> s1;
     cout << "Enter a string s2: ";
     cin >> s2;
 
     if (isAnagram(s1, s2)) cout << s1 << " and " << s2 << " are anagrams." << endl;
     else cout << s1 << " and " << s2 << " are not anagrams." << endl;

     system("pause");

    return 0;
}
