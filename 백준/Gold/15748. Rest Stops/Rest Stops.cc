#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<ll, ll> pii;

ll L, N;
ll Rf, Rb;
struct cmp {
    bool operator()(pii a, pii b) {
        // 가치가 같다면 높은 곳부터
        if (a.second == b.second) return a.first < b.first;
        // 가치 큰 곳부터
        return a.second < b.second;
    }
};
priority_queue<pii, vector<pii>, cmp> pq;
int main() {ios_base::sync_with_stdio(false); cout.tie(NULL); cin.tie(NULL);

cin >> L >> N >> Rf >> Rb;

for (int i = 0; i < N; ++i) {
    ll x, c;
    cin >> x >> c;
    pq.push(pii(x, c));
}

ll now = 0LL;// 현재 등산 위치
ll ans = 0LL;// 구하고자하는 답
while (!pq.empty()) {
    ll where = pq.top().first;
    ll value = pq.top().second;
    pq.pop();
    if (now >= where) continue;

    ans += (where - now) * (Rf - Rb) * value;
    now = where;
}
cout << ans << '\n';

return 0;
}