#include <iostream>
#include <cmath>
#include <algorithm>

void solve(long long w, long long h, long long n) {
    long long low = 0, high = std::max(w, h)*n;
    long long answer = 0;
    while (low <= high) {
        long long mid = low + (high - low) / 2;
        long long a = mid / w;
        long long b = mid / h;
        
        if (a * b >= n) {
            answer = mid;
            high = mid - 1;
        } else {
            low = mid + 1;
        }
    }

    std::cout << answer << std::endl;
}

int main() {
    long long w, h, n;
    std::cin >> w >> h >> n;

    solve(w, h, n);
}