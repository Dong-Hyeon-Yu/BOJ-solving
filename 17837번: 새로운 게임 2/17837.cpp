#include <iostream>
#include <vector>

#define vi vector<int>
#define vvi vector<vi>
#define vvv vector<vector<vector<int>>>
#define point pair<int, int>
#define WHITE 0
#define RED 1
#define BLUE 2

using namespace std;

vvi color;
vvv board;
int N, K;
point directions[] = {{0,0},{0,1},{0,-1},{-1,0},{1,0}};
int convert[] = {0, 2,1,4,3};
struct Horse {int r;int c;int d;};
vector<Horse> horses;

bool move(int idx, int r, int c, int d, bool flag=false) {
    int nr = r+directions[d].first;
    int nc = c+directions[d].second;

    if (!(0<=nr && nr<N && 0<=nc && nc<N) || color[nr][nc]==BLUE) {
        if (flag) 
            return false;  // stucked! do nothing
        else {
            horses[idx].d = convert[d];
            return move(idx, r,c,convert[d], true); // flip the direction
        }
            
    }
    else if (color[nr][nc]==RED) {
        for (int _ = board[r][c].size()-1; _>=0; _--) {
            // moving each horse from the top (reversed order)
            int tmp_horse_idx = board[r][c].back();
            horses[tmp_horse_idx] = {nr, nc, horses[tmp_horse_idx].d}; // moves with the same direction
            board[nr][nc].push_back(tmp_horse_idx); 
            board[r][c].pop_back();

            if (board[nr][nc].size()>=4) return true;
            if (tmp_horse_idx == idx) break;
        }

    }
    else if (color[nr][nc]==WHITE) {
        bool find = false;
        int cnt = 0;
        for (auto iter=board[r][c].begin(); iter!=board[r][c].end(); iter++) {
            // moving each horse from the bottom (same order)
            if (*iter == idx) find=true;
            if (find) {
                horses[*iter] = {nr, nc, horses[*iter].d};
                board[nr][nc].push_back(*iter);
                if (board[nr][nc].size()>=4) return true;
                ++cnt;
            }
        }
        while (cnt--) board[r][c].pop_back();
    }

    // 아래처럼 깔끔하게 가능!
    // vector<int>& old_pawn = pawn[x][y];
    // vector<int>& new_pawn = pawn[nx][ny];
    // auto pos = find(old_pawn.begin(), old_pawn.end(), i);
    // if(board[nx][ny] == 1) reverse(pos, old_pawn.end());
    // for(auto iter = pos; iter != old_pawn.end(); ++iter)
    // {
    //     new_pawn.push_back(*iter);
    //     v[*iter].x = nx;
    //     v[*iter].y = ny;
    // }
    // old_pawn.erase(pos, old_pawn.end());

    return false;
}

int main() {
    cin >> N >> K;
    color = vvi(N, vi(N, 0));
    board = vvv(N, vvi(N, vi()));

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> color[i][j];
        }
    }

    int r,c,d;
    for (int i=0; i<K; i++) {
        cin >> r >> c >> d;
        --r; --c; 
        horses.push_back({r,c,d});
        board[r][c].push_back(i);
    }

    int turn = 0;
    while (++turn < 1000) {
        for (int idx=0; idx<K; idx++) {
            if (move(idx, horses[idx].r, horses[idx].c, horses[idx].d)) {
                cout << turn; return 0;
            }
        }
    }

    cout << -1;
    return 0;
}