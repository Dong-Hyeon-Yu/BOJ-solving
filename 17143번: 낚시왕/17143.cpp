#include <iostream>
#include <vector>
#define vi vector<int>
#define vvs vector<vector<shark_info*>>
using namespace std;

struct shark_info {
    int r;
    int c;
    int speed;
    int di;
    int z;
    bool alive = true;
    int time = 0;
};

int R,C,M;
vector<shark_info*> sharks;

const int dr[] = {0,-1,1,0,0};
const int dc[] = {0,0,0,1,-1};
const int convert[] = {0, 2, 1, 4, 3};


void print(vvs &graph) {
    for (auto &row: graph) {
        for (auto shark: row) {
            cout << (shark?shark->z:0) << " " ;
        }
        cout << "\n";
    }
    cout << endl;
}

int main() {
    cin >> R >> C >> M;
    vvs graph = vvs(R+1, vector<shark_info*>(C+1, nullptr));

    int r,c,s,d,z;
    int tmp = M;
    while (tmp--) {
        cin >> r >> c >> s >> d >> z;
        shark_info* shark = new shark_info{r,c,s,d,z};
        graph[r][c] = shark;
        sharks.push_back(shark);
    }
    // print(graph);

    int time = 0;
    int ans = 0;
    while (time++ < C) {
        for (int r=1;r<=R;r++) {
            if (graph[r][time] != nullptr) {
                // cout << "catch! " << graph[r][time]->z << "\n";
                ans += graph[r][time]->z;
                graph[r][time]->alive = false;
                graph[r][time]=nullptr;
                break;
            }
        }
        
        for (int i=0; i<sharks.size(); i++) {
            if (!sharks[i]->alive) continue;
            shark_info *shark = sharks[i];
            int nr = shark->r + dr[shark->di] * (shark->speed%(2*(R-1)));
            int nc = shark->c + dc[shark->di] * (shark->speed%(2*(C-1)));

            while (true) {
                // printf("shark %d moves : (%d,%d) -> (%d,%d)\n", shark->z, shark->r, shark->c, nr,nc);
                if (nr < 1) {
                    nr = -nr+2;
                    shark->di = convert[shark->di];
                } else if (nc < 1) {
                    nc = -nc+2;
                    shark->di = convert[shark->di];
                } else if (nr > R) {
                    nr = R-(nr-R);
                    shark->di = convert[shark->di];
                } else if (nc > C) {
                    nc = C-(nc-C);
                    shark->di = convert[shark->di];
                } else break;
            }
            // printf("shark %d moves : (%d,%d) -> (%d,%d)\n", shark->z, shark->r, shark->c, nr,nc);
            
            if (graph[shark->r][shark->c]!=nullptr && graph[shark->r][shark->c]->time <= shark->time)
                graph[shark->r][shark->c] = nullptr;
            
            if (graph[nr][nc] != nullptr) {
                if (graph[nr][nc]->time < time) {
                    graph[nr][nc] = nullptr;
                } 
                else {
                    shark_info* another_shark = graph[nr][nc];
                    if (shark->z > another_shark->z) {
                        graph[nr][nc] = shark;
                        shark->time = time;
                        shark->r = nr;
                        shark->c = nc;
                        another_shark->alive = false;
                    }
                    else {
                        shark->alive = false;
                    }
                }
            }

            if (graph[nr][nc] == nullptr) {
                graph[nr][nc] = shark;
                shark->time = time;
                shark->r = nr;
                shark->c = nc;
            }
        }
        // print(graph);
    }

    cout << ans << endl;
    return 0;
}