#include <iostream>
#include <vector>
#include <algorithm>

#define vi vector<bool>
#define vvi vector<vi>
#define point pair<int, int>

using namespace std;

int N;
vvi b_board, g_board;
const int ROW=6; const int COL=4;
vector<vector<point>> block_type = {
    {{-1,-1}},
    {{0,0}},
    {{0,0}, {0,1}},
    {{0,0}, {1,0}},
};
int convert[] = {0,1,3,2};

void locate_block(vector<point> _block_type, int horizontal_index, vvi &board) {    
    int max_row = -1;
    for(int row = 0; row<ROW; row++) {
        bool find = true;
        for (auto [i, j]: _block_type) {
            int target_x = row+i;
            int target_y = horizontal_index+j;
            bool available = (target_x>=0 && target_x<ROW && target_y>=0 && target_y<COL && !board[target_x][target_y]);
            find &= available;
        }

        if (!find) break;

        max_row = max(max_row, row);
    }

    for (auto [i, j]: _block_type) board[max_row+i][horizontal_index+j] = true;
}


int process(vvi &board) {
    int cnt = 0;
    int row = ROW-1;
    while (row>=2) {
        bool full = true;
        for (bool unit: board[row]) full &= unit;
        if (full == true) {
            for (int i=0;i<COL; i++) board[row][i]=false;
            for (int _r=row; _r>0; _r--) for (int i=0;i<COL;i++) board[_r][i] = board[_r-1][i];
            for (int i=0;i<COL; i++) board[0][i]=false;
            ++cnt;
            ++row;
        } 

        --row;
    }

    while (row>=0) {
        bool blank = true;
        for (bool unit: board[row]) blank &= (unit==false);
        if (!blank) {
            for (int i=0; i<COL; i++) board[ROW-1][i]=false;
            for (int _r=ROW-1; _r>0; _r--) for (int i=0;i<COL;i++) board[_r][i] = board[_r-1][i];
            for (int i=0;i<COL; i++) board[0][i]=false;
            ++row;
        }
        --row;
    }

    return cnt;
}

void print(vvi &graph) {
    for(auto &row: graph) {
        for (auto item: row) cout << (item?1:0) << " ";
        cout << "\n";
    }
    cout << "\n";
}

int main() {
    g_board = vvi(6, vi(4, false));
    b_board = vvi(6, vi(4, false));

    cin >> N;
    int t,x,y;
    int ans = 0;
    for (int i=0; i<N; i++) {
        cin >> t >> x >> y;
        // printf("cmd : type(%d), x(%d), y(%d)\n", t,x,y);
        locate_block(block_type[t], y, g_board);
        // cout << "g_board after locate:\n";
        // print(g_board);
        locate_block(block_type[convert[t]], x, b_board);
        // cout << "b_board after locate:\n";
        // print(b_board);
        ans += process(g_board);
        // cout << "g_board after processing:\n";
        // print(g_board);
        
        ans += process(b_board);
        // cout << "b_board after processing:\n";
        // print(b_board);
    }
    cout << ans << "\n";
    int num_tiles = 0;
    for (int i=0; i<ROW; i++) {
        for (int j=0; j<COL; j++) {
            if (g_board[i][j]) num_tiles += 1;
            if (b_board[i][j]) num_tiles += 1;
        }
    }
    cout << num_tiles;

    return 0;
}