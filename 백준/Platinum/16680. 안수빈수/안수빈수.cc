#include <bits/stdc++.h>

#define FAST() cin.tie(0)->sync_with_stdio(0)
#define ALL(x) (x).begin(), (x).end()
#define SIZE(x) (int)((x).size())

#define deb(x) cout << #x << " : " << (x) << "\n"
#define deb_pair(x, y) cout << "(" << #x << ", " << #y << ") : (" << (x) << ", " << (y) << ")\n"
#define deb_triplet(x, y, z) cout << "(" << #x << ", " << #y << ", " << #z << ") : (" << (x) << ", " << (y) << ", " << (z) << ")\n"
#define deb_tuple(s) \
    cout << "["; \
    for (int __i = 0; __i < SIZE(s); __i++) { \
        cout << s[__i]; \
        if (__i != SIZE(s) - 1) cout << ", "; \
    } \
    cout << "]\n";

using namespace std;

int main() {
    FAST();
    int t;
    cin >> t;

    for (int i = 0; i < t;++i) {
        long long n;
        cin >> n;

        string N = to_string(n);
        string CUR = N + string(N.length(), '0');
        long long cur = stoll(CUR);
        long long tmp;
        bool key = true;
        while (true) {
            int cnt = 0;
            if (cur > 1e18) {
                break;
            }
            tmp = cur;
            while (tmp > 0) {
                cnt += tmp % 10;
                tmp = tmp / 10;
            }
            if (cnt % 2) {
                cout << cur << endl;
                key = false;
                break;
            } else {
                cur += n;
            }
        }
        if (key) {
            cout << -1 << endl;
        }

    }
}
