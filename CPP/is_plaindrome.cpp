/***
 * function : 
 *     bool is_plaindrome(string)
 * Description:
 *     這是使用 遞迴 方式 寫成檢查字串是否是迴文的 function is_plaindrome
 * Algorithm:
 *     1. 終止條件: 
 *        1.1 字串長度為1時 即為迴文
 *        1.2 字串長度為2時 如果是重複的字元，即為迴文，否則不是
 *     2. 遞迴: 當字串檢查頭尾一致時，則遞迴檢查去除頭尾後的字串是否為迴文
 * 
 */

using namespace std;
#include <iostream>

bool is_plaindrome(string text) {
    int length = text.length();

    if (length == 1) return true; // 只有一個字母必是迴文字串
    if (length == 2) return (text.at(0) == text.at(1)); // 只有兩個字母時，只要字母相同便是迴文字串
    // 開頭與結尾字母若相同，則去掉頭尾後繼續判斷新的字串是否也是迴文字串, 此處用遞迴法來檢查結果
    if (text.at(0) == text.at(length-1))  return is_plaindrome(text.substr(1, length-2));
    else return false; 
}

int main() {
    cout << "This is a checking function for judging a string to see if it is a plaindrome(迴文)."<<endl;
    cout << "-----------------------------------" <<endl;

    cout << "Input a String : ";
    string s;
    cin >> s;
    // Add boolalpha to covert bool value(0,1) to boolean string
    cout << "The String " << s << " is a plaindrome ? " << boolalpha << is_plaindrome(s) << endl;

    return 0;
}