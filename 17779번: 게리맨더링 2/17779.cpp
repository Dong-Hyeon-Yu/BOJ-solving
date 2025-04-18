#include <iostream>
#include <vector>

#define vi vector<int>
#define vvi vector<vi>

using namespace std;

int N;

inline bool boundary_check(int i, int j) {
    return 1 <= i && 1<=j && i<=N && j<=N;
}

int compute_diff(vvi &graph, int x, int y, int d1, int d2) {
    // cout << "\ncompute diff" << x << y << d1 << d2 << endl;
    int cnt_of[] = {0,0,0,0,0};
    int tmp;
    for (int r=1; r<=N; r++) {
        for (int c=1; c<=N; c++) {
            if (1<=r && r<x+d1 && 1<=c && c <=y && c<-r+x+y) tmp=0;
            else if (1<=r && r<=x+d2 && y<c && c<=N && c>r+y-x) tmp=1;
            else if (x+d1<=r && r<=N && 1<=c && c<y-d1+d2 && c<r+y-x-2*d1) tmp=2;
            else if (x+d2<r && r<=N && y-d1+d2<=c && c<=N && c>-r+x+y+2*d2) tmp=3;
            else tmp=4;

            cnt_of[tmp] += graph[r][c];
            // cout << tmp << " ";
        }
        // cout << "\n";
    }
    int maxv=-1;
    int minv=123456789;
    for (int i=0; i<5; i++) {
        int cnt = cnt_of[i];
        // cout << cnt << "(" << i << ") ";
        if (cnt == 0) return -1;
        minv = min(minv, cnt);
        maxv = max(maxv, cnt);
    }
    // cout << "\n" << endl;
    
    return maxv-minv;
}

int main() {
    cin >> N;
    vvi graph = vvi(N+1, vi(N+1, 0));
    for(int i=1; i<=N; i++) for(int j=1; j<=N; j++) cin >> graph[i][j];
    
    int ans = 123456789;
    for(int x=1; x<N; x++) {
        for (int y=1; y<N; y++) {
            for (int d1=1; boundary_check(x+d1, y-d1); d1++) {
                for (int d2=1; boundary_check(x+d2, y+d2); d2++) {
                    if (!boundary_check(x+d1+d2, y-d1+d2)) break;

                    int diff = compute_diff(graph,x,y,d1,d2);
                    if (diff == -1) continue;
                    ans = min(diff, ans);
                }
            }
        }
    }

    cout << ans;
    return 0;
}