#include <iostream>
#include <vector>
#include <queue>

#define point pair<int, int> 
#define vvi vector<vector<int>>
#define MAX 100000000

using namespace std;

int N;
vvi graph;
point shark;
const point directions[] = {{0,1}, {0,-1},{1,0},{-1,0}};

int bfs(vvi&, vvi&, int);


int main() {
    cin >> N;
    graph = vvi(N, vector<int>(N));
    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            cin >> graph[i][j];
            if (graph[i][j] == 9) {
                shark = {i, j};
                graph[i][j] = 0;
            }
        }
    }

    vvi visited(N, vector<int>(N));
    int seconds = 0, sec = 0;
    int num_of_eating = 0, shark_value = 2;
    while (true) {
        for (int i=0; i<N; i++) {
            fill(visited[i].begin(), visited[i].end(), MAX);
        }
        
        if (sec = bfs(visited, graph, shark_value)) {
            num_of_eating += 1;
            seconds += sec;
            if (num_of_eating == shark_value) {
                ++shark_value;
                num_of_eating = 0;
            }
        }
        else {
            cout << seconds << endl;
            break;
        }
    }

    return 0;
}

int bfs(vvi &visited, vvi &graph, int shark_value) {
    priority_queue<pair<int, point>> queue;
    queue.push({0, shark});
    visited[shark.first][shark.second] = 0;
    int min_dist = MAX;

    while (!queue.empty()) {
        auto [dist, cur] = queue.top();
        queue.pop();

        dist = -1 * dist;
        
        if (dist > min_dist) continue;
        
        int v = graph[cur.first][cur.second];
        if (0<v && v<shark_value) {
            min_dist = min(min_dist, dist);
        }

        int ndist = dist + 1;

        for (auto di : directions) {
            int nr = cur.first + di.first;
            int nc = cur.second + di.second;
            if (0<=nr && 0<=nc && nr<N && nc<N && graph[nr][nc]<=shark_value) {
                if (visited[nr][nc] > ndist) {
                    visited[nr][nc] = ndist;
                    queue.push({-ndist, {nr, nc}});
                }
            }
        }
    }

    for (int i=0; i<N; i++) {
        for (int j=0; j<N; j++) {
            if (min_dist<MAX && min_dist==visited[i][j]) { 
                if (graph[i][j] < shark_value && 0< graph[i][j]) {
                    graph[i][j] = 0;
                    shark = {i, j};
                    return min_dist;
                }
            }
        }
    }

    return 0;
}