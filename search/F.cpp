#include <iostream>
#include <algorithm>

void solve(int N, int x, int y) {
    long low = 0; long high = N * std::max(x, y);
    long answer = low;

    while (low <= high) {
        long mid = low + (high - low) / 2;

        if (mid / x + mid / y >= N - 1) {
            answer = std::min(x,y) + mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }
    std::cout << answer << std::endl;
}

int main () {
    int N, x, y;
    std::cin >> N >> x >> y;
    
    solve(N, x, y);
}
