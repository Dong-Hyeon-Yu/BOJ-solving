#include <iostream>
#include <vector>
#include <queue>
#define vi vector<int>
#define vvi vector<vi>
#define UNVISITED -123456789
#define VIRUS 2
#define point pair<int,int>
using namespace std;


void combination(vector<vector<point>> &container, vector<point> const &viruses, int target_size, int next, vector<point> tmp) {
    if (tmp.size() == target_size) {
        container.push_back(tmp);
        return;
    }

    for (int k=next;k<viruses.size();k++) {
        tmp.push_back(viruses[k]);
        combination(container, viruses, target_size, k+1, tmp);
        tmp.pop_back();
    }
}


int main() {
    int N,M;
    cin >> N >> M;
    vvi graph = vvi(N, vi(N, 0));

    vector<point> viruses;
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> graph[i][j];
            if (graph[i][j] == 0) graph[i][j] = UNVISITED;
            else if (graph[i][j] == VIRUS) viruses.emplace_back(i, j);
        }
    }

    vector<vector<point>> combinations;
    vector<point> tmp;
    combination(combinations, viruses, M, 0, tmp);
    // for (auto &virus: viruses) {
    //     printf("(%d, %d) ", virus.first, virus.second);
    // }
    // cout << endl;
    // for (auto &combo: combinations) {
        // for (auto p: combo) printf("(%d, %d) ", p.first, p.second);
        // cout << endl;
    // }
    int min_time = 123456789;
    point directions[4] = {{1,0},{-1,0},{0,1},{0,-1}};

    for(auto& combo: combinations) {
        
        vvi visited = vvi(graph);
        int max_dist = 0;
        queue<pair<point, int>> que;
        for (auto& virus: combo) {
            que.emplace(virus, 0);
            visited[virus.first][virus.second] = UNVISITED;
        }

        // for (auto p: combo) printf("(%d, %d) ", p.first, p.second);
        // cout << endl;

        while (!que.empty()) {
            auto [cur, dist] = que.front(); que.pop();

            if (min_time<-dist) break;

            // printf("current (%d, %d) min_time: %d", cur.first, cur.second, min_time);
            
            int cur_value = visited[cur.first][cur.second];
            if (!(cur_value == UNVISITED || cur_value == VIRUS)) continue;
            if (cur_value == UNVISITED) {
                max_dist = max(max_dist, -dist);
            }
            visited[cur.first][cur.second] = -dist;

            for (auto &[dx, dy]: directions) {
                int nx = cur.first + dx;
                int ny = cur.second + dy;
                if (nx>=0 && ny>=0 && nx<N && ny<N) {
                    if (visited[nx][ny]==VIRUS || visited[nx][ny]==UNVISITED) {
                        que.push({{nx,ny}, dist-1});
                        // printf("next (%d, %d) ", nx,ny);
                    }
                }
            }
        }
        // cout << max_dist << endl;
        // for(auto& row: visited) {
        //     for (auto& item: row) cout << item << " ";
        //     cout << endl;
        // }
        // for(auto& row: graph) {
        //     for (auto& item: row) cout << item << " ";
        //     cout << endl;
        // }

        for (int i=0;i<N;i++){
            for (int j=0;j<N;j++) {
                if (visited[i][j]==UNVISITED && graph[i][j]==UNVISITED) {
                    max_dist = min_time;
                }
            }
            if (max_dist==min_time) break;
        }
        // cout << "max_dist: " << max_dist << endl;
        min_time = min(min_time, max_dist);
    }
    
    cout << (min_time==123456789?-1:min_time);

    return 0;
}