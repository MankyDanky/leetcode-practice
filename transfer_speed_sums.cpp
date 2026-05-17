#include <bits/stdc++.h>
#define ll long long

using namespace std;

ll res = 0;
const int INF = INT_MAX>>1;

class DSU {
public:
    vector<int> rank;
    vector<int> par;
    vector<int> rep;
    int n;

    DSU(int n) {
        this->rank.resize(n, 1);
        this->par.resize(n);
        this->rep.resize(n, INF);
        for (int i = 0; i < n; i++) {
            par[i] = i;
        }
        this->n = n;
    }

    int Find(int i) {
        int res = i;
        while (par[res] != res) {
            par[res] = par[par[res]];
            res = par[res];
        }
        return res;
    }

    bool Union(int n1, int n2, int cap) {
        int p1, p2;
        p1 = Find(n1);
        p2 = Find(n2);
        if (p1 == p2) {
            return false;
        }

        if (rank[p1] > rank[p2]) {
            rep[p1] = min(min(rep[p1], rep[p2]), cap);
            res += (ll)rep[p1] * rank[p1] * rank[p2];
            rank[p1] += rank[p2];
            par[p2] = p1;
        } else {
            rep[p2] = min(min(rep[p1], rep[p2]), cap);
            res += (ll)rep[p2] * rank[p1] * rank[p2];
            rank[p2] += rank[p1];
            par[p1] = p2;
        }
        return true;
    }
};

int main() {
    int n;
    cin>>n;

    DSU dsu(n);

    vector<tuple<int,int,int>> edges;
    for (int i = 0; i < n-1; i++) {
        
        int a, b, x;
        cin>>a>>b>>x;
        a--;b--;
        edges.emplace_back(x, a, b);
    }

    sort(edges.begin(), edges.end());

    reverse(edges.begin(), edges.end());

    for (int i = 0; i < n-1; i++) {
        auto [x, a, b] = edges[i];
        dsu.Union(a, b, x);
    }

    cout<<res<<endl;


    return 0;
}