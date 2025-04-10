#include <iostream>
#include <vector>
#include <set>
#include <numeric>
#define vi vector<int>
#define vvi vector<vi>
#define point pair<int, int>

using namespace std;
int R, C, T;
const int dx[] = {0,0,1,-1};
const int dy[] = {1,-1,0,0};
set<point> robot;


void disperse_dust(vvi &graph) {
    vvi delta = vvi(R, vi(C, 0));
    int candidates;
    for (int i=0;i<R;i++) {
        for (int j=0;j<C;j++) {
            if (graph[i][j]==0) continue;

            candidates=0;
            int dust_delta = graph[i][j]/5;
            for (int _=0;_<4;_++) {
                int di = i + dx[_];
                int dj = j + dy[_];
                if (0<=di && di<R && 0<=dj && dj<C && robot.find({di, dj}) == robot.end()) {
                    ++candidates;
                    delta[di][dj] += dust_delta;
                }
            }


            delta[i][j] -= int(graph[i][j]/5) * candidates;
        }
    }

    for (int i=0;i<R;i++) for (int j=0;j<C;j++) graph[i][j] += delta[i][j];
}

void clean_air(vvi &graph, int lower, int upper) {
    for (int i=upper-1; i>0; i--) graph[i][0] = graph[i-1][0];
    for (int j=0; j<C-1; j++) graph[0][j] = graph[0][j+1];
    for (int i=0; i<upper; i++) graph[i][C-1] = graph[i+1][C-1];
    for (int j=C-1; j>0; j--) graph[upper][j] = graph[upper][j-1];
    
    for (int i=lower+1; i<R-1; i++) graph[i][0] = graph[i+1][0];
    for (int j=0; j<C-1; j++) graph[R-1][j] = graph[R-1][j+1];
    for (int i=R-1; i>lower; i--) graph[i][C-1] = graph[i-1][C-1];
    for (int j=C-1; j>0; j--) graph[lower][j] = graph[lower][j-1];
}

void print_graph(vvi &graph, int flag) {
    if (flag==1) cout << "After disperse:\n";
    else cout << "After air clean:\n" ;

    for (int i=0; i<R; i++) {
        for (int j=0; j<C; j++) {
            cout << graph[i][j] << " ";
        }
        cout << "\n";
    }
    cout << endl;
}

int main() {
    cin >> R >> C >> T;

    int lower=-1, upper = -1;
    vvi graph = vvi(R, vi(C, 0));
    for (int i=0; i<R; i++) {
        for (int j=0; j<C; j++) {
            cin >> graph[i][j];
            if (graph[i][j]==-1) {
                graph[i][j] = 0;
                robot.insert({i, j});
                if (upper>0) lower = i;
                else upper = i;
            }
        }
    }

    int time = 0;
    while (T>time) {
        disperse_dust(graph);
        // print_graph(graph, 1);

        clean_air(graph, lower, upper);
        // print_graph(graph, 2);
        ++time;
    }

    int ans = 0;
    for (auto& row: graph) for (auto& ele: row) ans += ele;
    cout << ans << endl;

    return 0;
}