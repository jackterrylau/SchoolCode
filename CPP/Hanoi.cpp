/***
 * 
 * Hanoi 河內塔:
 *     河內塔問題共有三個步驟, 先把頂層 n-1 個 盤子 由 開始柱(From) 經由 目標柱(To) 搬到 中間柱(Assist),
 *     再將最底層的 唯 1 個 盤子 直接由 開始柱(From) 搬到 目標柱(To)
 *     最後再把 在中間柱(Assist) 的 頂層 n-1 個 盤子 經由 開始柱(From) 搬到 目標柱(To)
 * 
 */

#include <string>
#include <iostream>
using namespace std;

int step = 1;

void Hanoi(int dashs, char from, char assist, char to, int moved_dash) {
    if (dashs > 1) { 
        // 上層的 n-1 個 dashs 先從 from 搬到 assist, 此時靠 to 輔助
        Hanoi(dashs-1, from, to, assist, dashs-1);
        // 直接移動最底層的盤子到目標柱
        Hanoi(1, from, assist, to, moved_dash);
        // 上層的 n-1 個 dashs 接著從 assist 搬到 to, 此時靠 from 輔助
        Hanoi(dashs-1, assist, from, to, dashs-1);
    }
    // 只有一個 dash 時 直接從 from 到 to
    if (dashs == 1) {
        // 只有當真的移動 1 個 dash 時 才 算完成一個步驟
        cout << "Step " << step++ 
             << ". The dash " << moved_dash << " is moved from pillar " << from << " to pillar " << to << ". " << endl;
    }
}

int main() {
    int dashs, moved_dash;
    char pillar_from='A', pillar_assist='B', pillar_to='C';
    cout << "Input a dash number for moving in Hanoi Game: ";
    cin>> dashs;
    cout <<"Your "<< dashs << " dashs are moved in Hoaoi by below path:" << endl
         << "##############################################" << endl;

    moved_dash = dashs;
    Hanoi(dashs, pillar_from, pillar_assist, pillar_to, moved_dash);

    cout << "##############################################" << endl;

    return 0;
}