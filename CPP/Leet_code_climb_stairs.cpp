#include <iostream>
using namespace std;

class Solution {
public:
    Solution() {};

    long climbStairs(int n) {
        /***
        if (n == 1) return 1;
        if (n == 2) return 2;
        return (climbStairs(n - 1) + climbStairs(n - 2));
        ***/

        //Initialize stairs storage
        long stairs[n+1];
        for (int i = 0; i<n+1; i++) stairs[i] = 0;

        //Find result
        for (int s=1; s<n+1; s++) {
            if(s==1) stairs[s] = 1;
            if(s==2) stairs[s] = 2;
            if(s>=3) stairs[s] = stairs[s-1] + stairs[s-2];
        }

        return stairs[n];
    }
};

int main() {
    int n;
    cout<<"這是一個爬樓梯的遊戲，請輸入要爬的樓梯階數 n，一步只可以走1階或2階，然後輸出全部的爬樓梯方法."<<endl;
    cout<<"Input n = ";
    cin>>n;

    Solution sol;
    cout<<"爬"<<n<<"階樓梯 總共有 "<<sol.climbStairs(n)<<" 方式.";
    cin.get();
    
    return EXIT_SUCCESS;
}
