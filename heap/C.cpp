#include <iostream>
#include <vector>
#include <string>
using namespace std;

vector<long long> h;

void siftUp(int i) {
    while (i > 0) {
        int p = (i - 1) / 2;
        if (h[i] >= h[p]) break;
        swap(h[i], h[p]);
        i = p;
    }
}

void siftDown(int i) {
    int n = h.size();
    while (true) {
        int l = 2 * i + 1, r = 2 * i + 2, m = i;
        if (l < n && h[l] < h[m]) m = l;
        if (r < n && h[r] < h[m]) m = r;
        if (m == i) break;
        swap(h[i], h[m]);
        i = m;
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string cmd;
    while (cin >> cmd) {
        if (cmd == "CLEAR") {
            h.clear();
        } else if (cmd == "ADD") {
            long long x;
            cin >> x;
            h.push_back(x);
            siftUp(h.size() - 1);
        } else {  // EXTRACT
            if (h.empty()) {
                cout << "CANNOT\n";
            } else {
                cout << h[0] << '\n';
                h[0] = h.back();
                h.pop_back();
                if (!h.empty()) siftDown(0);
            }
        }
    }
    return 0;
}