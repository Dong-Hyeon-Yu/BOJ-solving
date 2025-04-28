#include <iostream>
#include <vector>
#define point pair<int, int>
#define vi vector<int>
#define vvi vector<vi>
#define SHARK 0

using namespace std;

struct Fish {
    int r; int c; int d; int no;
    bool alive = true;
};
vector<Fish> fishes = vector<Fish>(17);
vvi graph = vvi(4, vi(4,0));
point directions[] = {{-1,0},{-1,-1},{0,-1},{1,-1},{1,0},{1,1},{0,1},{-1,1}};


inline void swap(Fish &a, Fish &b, vvi &graph) {
    graph[a.r][a.c] = b.no;
    graph[b.r][b.c] = a.no;
    std::swap(a.r, b.r);
    std::swap(a.c, b.c);
}

inline int eat_fish(Fish &shark, Fish &a, vvi &graph) {
    a.alive = false;
    shark.d = a.d;
    swap(shark, a, graph);

    return a.no;
}
inline void unwind_eating(Fish &shark, Fish &a, vvi &graph, int prev_d) {
    a.alive = true;
    shark.d = prev_d;
    swap(shark, a, graph);
}

void move_fishes(vvi &graph, vector<Fish> &fishes) {
    for (int i=1; i<17; i++) {
        if (!fishes[i].alive) continue;

        int r = fishes[i].r;
        int c = fishes[i].c;
        for (int _d=0; _d<8; _d++) {
            int nd = (fishes[i].d+_d)%8;
            int nr = r + directions[nd].first;
            int nc = c + directions[nd].second;
            if (nr>=0 && nr<4 && nc>=0 && nc<4 && graph[nr][nc]!=SHARK) {
                fishes[i].d = nd;
                // printf("swap: %d(%d,%d) <--> %d(%d,%d)\n", graph[r][c],fishes[i].r,fishes[i].c,graph[nr][nc],nr,nc);
                swap(fishes[i], fishes[graph[nr][nc]], graph);
                // printf("\tAfter swap: %d(%d,%d) >--< %d(%d,%d)\n", graph[r][c],fishes[graph[r][c]].r,fishes[graph[r][c]].c,graph[nr][nc],fishes[graph[nr][nc]].r,fishes[graph[nr][nc]].c);
                
                break;
            }
        }
    }
}

void print(vvi &graph, vector<Fish> &fishes) {
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            cout << (fishes[graph[i][j]].alive ? graph[i][j] : -1) << " ";
        }
        cout << "\n";
    }
    cout << "\n";
}

int dfs(vvi &_graph, vector<Fish> &_fishes) {
    vvi graph = vvi(_graph);
    vector<Fish> fishes = vector<Fish>(_fishes);
    move_fishes(graph, fishes);
    // cout << "After moves: \n";
    // print(graph, fishes);

    Fish shark = fishes[0];
    // printf("shark (%d,%d) heading (%d,%d)\n", shark.r, shark.c, directions[shark.d].first, directions[shark.d].second);
    int fish_eaten = 0;
    for (int i=1;i<4;i++) {
        int nr = shark.r + directions[shark.d].first*i;
        int nc = shark.c + directions[shark.d].second*i;
        if (nr>=0 && nc>=0 && nr<4 && nc<4 && fishes[graph[nr][nc]].alive) {
            int target_no = fishes[graph[nr][nc]].no;
            // cout << "shark eats the fish(" << target_no << ") \n";
            fish_eaten = max(fish_eaten, eat_fish(fishes[SHARK], fishes[graph[nr][nc]], graph) + dfs(graph, fishes));
            // cout << "unwinding " << target_no << "\n";
            unwind_eating(fishes[SHARK], fishes[target_no], graph, shark.d);
        }
    }

    return fish_eaten;
}

int main() {
    int a, b;
    for (int i=0; i<4; i++) {
        for (int j=0; j<4; j++) {
            cin >> a >> b;
            fishes[a] = Fish {i,j,b-1,a};
            graph[i][j] = a;
        }
    }
    fishes[0] = Fish {0,0,0,SHARK};

    int ans = 0;
    ans += eat_fish(fishes[SHARK], fishes[graph[0][0]], graph);
    // print(graph, fishes);

    //dfs
    ans += dfs(graph, fishes);

    cout << ans;
    return 0;
}