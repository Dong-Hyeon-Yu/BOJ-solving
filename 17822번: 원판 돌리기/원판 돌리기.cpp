/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 17822                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: ydh9516 <boj.kr/u/ydh9516>                  +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/17822                          #+#        #+#      #+#    */
/*   Solved: 2025/04/21 17:37:47 by ydh9516       ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */
#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>

#define point pair<int, int>
#define CLOCK 0
#define COUTER_CLOCK 1
#define NOENTRY -1

using namespace std;

int N,M,T;
vector<vector<int>> board;
vector<int> cnt;

void rotate(int x, int d, int k) {
    if (k > int(M/2)) {
        d = 1-d; // reverse
        k = M-k;
    }
    // printf("[rotating] direction: %d, cnt: %d\n", d, k);


    for (int multiplier=x; multiplier<=N; multiplier+=x) {
        int idx = multiplier-1;
        int _k = k;
        
        if (d==CLOCK) {
            std::rotate(board[idx].begin(), board[idx].end()-_k, board[idx].end());
            // board[idx].push_front(board[idx].back());
            // board[idx].pop_back();
        }
        else {
            std::rotate(board[idx].begin(), board[idx].begin()+_k, board[idx].end());
            // board[idx].push_back(board[idx].front());
            // board[idx].pop_front();
        }
        
    }
}

point directions[] = {{0,1}, {0,-1},{1,0}, {-1,0}};
void dfs(int i, int j, int key, vector<vector<bool>> &visited, vector<point> &ans) {
    ans.emplace_back(i,j);
    visited[i][j] = true;

    for (auto [di, dj]: directions) {
        int ni = i+di;
        int nj = j+dj;
        if (0>nj) nj += M;
        else if (M<=nj) nj -= M;
        
        if (0<=ni && ni<N && board[ni][nj]==key && !visited[ni][nj]) 
            dfs(ni,nj,key,visited,ans);
    } 
}

void process_adjacents() {
    bool flag = false;
    int total = 0;
    
    vector<vector<bool>> visited = vector<vector<bool>>(N, vector<bool>(M, false));
    for (int i=0; i<N; i++){
        for (int j=0; j<M; j++) {
            if (board[i][j]==NOENTRY) continue;

            total += board[i][j]; // in case of no (adjacent && indentical) items

            vector<point> points;
            if (!visited[i][j]) dfs(i,j, board[i][j], visited, points);
            if (points.size()>1) {
                flag = true;
                for (auto &p: points) {
                    board[p.first][p.second] = NOENTRY;
                    cnt[p.first] -= 1;
                }
            }
        }
    }
    

    if (flag == false) {
        int total_cnt =0;
        for (int i=0; i<N; i++) total_cnt += cnt[i];
        double avg = (double)total / total_cnt;
        // printf("[processing] cnt:%d, sum:%d, avg:%.2f\n", total_cnt, total, avg);

        for (int i=0; i<N; i++){
            for (int j=0; j<M; j++) {
                if (board[i][j]==NOENTRY) continue;

                if (board[i][j]>avg) board[i][j] -= 1;
                else if (board[i][j]<avg) board[i][j] += 1;
            }
        }
    }
}

void print_board() {
    for (auto& circle: board) {
        for (int num: circle) {
            cout << num << " ";
        }
        cout << "\n";
    }
}

int main() {

    cin >> N >> M >> T;
    board = vector<vector<int>>(N, vector<int>(M, 0));
    cnt = vector<int>(N, M);

    for (int i=0; i<N; i++) for (int j=0; j<M; j++) cin >> board[i][j];

    int x,d,k;
    while (T--) {
        cin >> x >> d >> k;
        rotate(x,d,k);
        // printf("After rotate(%d,%d,%d):\n", x,d,k);
        // print_board();
        // printf("After processing(%d,%d,%d):\n", x,d,k);
        process_adjacents();
        // print_board();
    }

    int ans = 0;
    for (auto &circle: board) {
        for (int num: circle) {
            if (num==NOENTRY) continue;

            ans += num;
        }
    }

    cout << ans;


    return 0;
}