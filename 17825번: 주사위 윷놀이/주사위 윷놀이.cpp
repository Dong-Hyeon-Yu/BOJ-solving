/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 17825                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/17825                          #+#        #+#      #+#    */
/*   Solved: 2025/04/21 17:37:20 by ydh9516       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <iostream>
#include <vector>
#include <algorithm>
#define point pair<int,int>
#define FINAL_TURN 10
#define ARRIVE 0
#define START -1

using namespace std;

const int NUM_HORSES = 4;
int dices[10] = {0, };
int ans = 0;
const vector<vector<int>> path = {
    {START,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38}, // 21 size
    {13,16,19}, // (0,5) -> (1,x) 
    {22,24}, // (0,10) -> (2,x) 
    {28,27,26}, // (0,15) -> (3,x) 
    {25,30,35},
    {40,ARRIVE}
};
vector<point> horses = vector<point>(NUM_HORSES, {0,0});

inline point move_horse(int horse, int turn) {
    auto [i, j] = horses[horse];
    if (path[i][j]==ARRIVE) return {-1, -1};

    int prev_i = i; int prev_j = j;
    int remains_to_move = dices[turn];
    if (i==0) {
        if (j==5) {
            i=1;j=0;
        }
        else if (j==10) {
            i=2;j=0;
        }
        else if (j==15) {
            i=3;j=0;
        }
        remains_to_move-=1;
    }
    

    if (remains_to_move>0 && (i==1||i==2||i==3)) {
        int possible_move = path[i].size()-j-1;
        if (possible_move < remains_to_move) {
            remains_to_move -= possible_move+1;
            i=4;j=0;
        }
        else {
            j += remains_to_move;
            remains_to_move=0;
        }
    }

    if (remains_to_move>0 && (i==4||i==0)) {
        int possible_move = path[i].size()-j-1;
        if (possible_move < remains_to_move) {
            remains_to_move -= possible_move+1;
            i=5;j=0;
        }
        else {
            j += remains_to_move;
            remains_to_move=0;
        }
    }

    if (remains_to_move>0 && i==5) 
        j=1;
    
    
    if (path[i][j]!=ARRIVE) {
        for (int hidx=0; hidx<NUM_HORSES; hidx++) {
            if (hidx == horse) continue;
    
            auto [ai, aj] = horses[hidx];
            if (ai==i && aj==j) return {-1, -1};
        }
    } 

    horses[horse].first=i;
    horses[horse].second=j; 
    return {prev_i, prev_j};
}

void cartesian_product_of_horses(int sum=0, int turn=0) {
    if (turn == FINAL_TURN) {
        if (ans<sum) ans = sum;
    }
    else {
        for (int i=0; i<NUM_HORSES; i++) {
            auto [prev_i, prev_j] = move_horse(i, turn);
            if (prev_i != -1) {
                point &horse = horses[i];
                cartesian_product_of_horses(sum + path[horse.first][horse.second], turn+1);
                horse.first = prev_i;
                horse.second = prev_j;
            }
        }
    }
}

int main() {
    for(int i=0; i<FINAL_TURN; i++) cin >> dices[i];
    cartesian_product_of_horses();

    cout << ans;

    return 0;
}