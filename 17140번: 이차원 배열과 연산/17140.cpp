#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#define vvi vector<vector<int>>
#define vi vector<int>
#define pii pair<int,int>

using namespace std;


void sort_row(vvi &graph) {
    size_t max_row = 0;

    for (int row_idx=0; row_idx<graph.size(); row_idx++) {
        map<int, int> counter;
        for (auto &item: graph[row_idx]) {
            if (item == 0) continue;
            ++counter[item];
        }

        vector<pii> tmp(counter.begin(), counter.end());
        sort(tmp.begin(), tmp.end(), [](pii &a, pii &b)->bool {
            if (a.second == b.second) return a.first < b.first;
            else return a.second < b.second;
        } );
        vi new_row;
        for_each(tmp.begin(), tmp.end(), [&new_row](pii &pair){
            new_row.emplace_back(pair.first);
            new_row.emplace_back(pair.second);
        });

        max_row = max(max_row, new_row.size());
        graph[row_idx].clear();
        graph[row_idx].shrink_to_fit();
        for(int i=0;i<min(new_row.size(), size_t(100)); i++) {
            graph[row_idx].emplace_back(new_row[i]);
        }
    }

    for (int row_idx=0; row_idx<graph.size(); row_idx++) {
        if (max_row > graph[row_idx].size()) {
            size_t tmp = max_row - graph[row_idx].size();
            while (tmp--) graph[row_idx].emplace_back(0);
        }
    }
}

void transpose(vvi &graph) {
    vvi tmp = vvi(graph[0].size(), vi(graph.size()));
    for (int i=0;i<graph.size();i++) 
        for (int j=0;j<graph[0].size();j++) 
            tmp[j][i] = graph[i][j];

    // for (int i=0;i<graph.size();i++) 
    //     for (int j=0;j<graph[0].size();j++) 
    //     graph[i][j] = tmp[i][j];
    graph = tmp;
}

void sort_col(vvi &graph) {
    transpose(graph);
    sort_row(graph);
    transpose(graph);
}

int main() {
    int R,C,K;
    cin >> R >> C >> K;
    vector<vector<int>> graph = vvi(3, vi(3,0));
    for (int i=0; i<3; i++) {
        for (int j=0; j<3; j++) {
            cin >> graph[i][j];
        }
    }

    --R; --C;
    int time = 0;
    while (time<=100) {
        int row_size = graph.size();
        int col_size = graph[0].size();

        if (row_size>R && col_size>C && graph[R][C]==K) break;

        if (row_size>=col_size) sort_row(graph);
        else sort_col(graph);

        ++time;
    }

    cout << (time>100?-1:time) << endl;
    return 0;
}