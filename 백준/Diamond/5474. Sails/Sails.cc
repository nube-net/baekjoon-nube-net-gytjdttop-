#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

class FastNegativeIndexTracker {
public:
    vector<int> arr;
    set<int> negative_indices;

    FastNegativeIndexTracker(vector<int>& input) {
        arr = input;
        for (size_t i = 0; i < arr.size(); ++i) {  
            if (arr[i] < 0) {
                negative_indices.insert(i);
            }
        }
    }

    void update(int index, int delta) {
        int prev_value = arr[index];
        int new_value = prev_value + delta;

        if (prev_value < 0) {
            negative_indices.erase(index);
        }

        arr[index] = new_value;

        if (new_value < 0) {
            negative_indices.insert(index);
        }
    }

    vector<int> get_negative_indices() {
        return vector<int>(negative_indices.begin(), negative_indices.end());
    }

    int get_max_negative_index_less_than(int x) {
        auto it = negative_indices.lower_bound(x);
        if (it == negative_indices.begin()) return -1;
        return *(--it);
    }

    int get_min_negative_index_more_than(int x) {
        auto it = negative_indices.upper_bound(x);
        if (it == negative_indices.end()) return -1;
        return *it;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<pair<int, int>> a(n);
    for (size_t i = 0; i < n; ++i) { 
        cin >> a[i].first >> a[i].second;
    }

    sort(a.begin(), a.end());  

    vector<int> dp(a.back().first + 2, 0);
    dp[1] = -1;
    FastNegativeIndexTracker tracker(dp);

    for (auto& p : a) {
        int h = p.first;
        int c = p.second;

        int mid = tracker.get_max_negative_index_less_than(h + 1);
        if (mid == -1) mid = 1;

        if (h - mid + 1 >= c) {
            tracker.update(mid, 1);
            tracker.update(mid + c, -1);
        } else {
            mid = tracker.get_min_negative_index_more_than(h - c);
            if (mid == -1) mid = 1;
            tracker.update(mid, 1);
            tracker.update(h + 1, -1);
            int val = c - (h + 1 - mid);
            if (val > 0) {
                int mid2 = tracker.get_max_negative_index_less_than(h - c + 1);
                if (mid2 == -1) mid2 = 1;
                tracker.update(mid2, 1);
                tracker.update(mid2 + val, -1);
            }
        }
    }

    dp = tracker.arr;
    dp[0] = 1;
    for (size_t i = 1; i < dp.size(); ++i) {
        dp[i] = dp[i - 1] + dp[i];
    }

    long long ans = 0;
    for (size_t i = 1; i < dp.size(); ++i) {  
        ans += (long long)dp[i] * (dp[i] - 1) / 2;
    }

    cout << ans << "\n";

    return 0;
}
