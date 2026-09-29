#include <iostream>
#include <vector>
#include <cmath>

void solve(std::vector<int> &stoils, int N, int K) {
    int low = 1, high = stoils[N - 1] - stoils[0];
    int distance = 0;

    while (low <= high) {
        int mid = low + (high - low) / 2;
        int answer = low;

        int count = 1;
        int last_position = stoils[0];
        for (int i = 1; i < N; i++) {
            if (stoils[i] - last_position >= mid) {
                count++;
                last_position = stoils[i];
            }
        }

        if (count >= K) {
            distance = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    std::cout << distance << std::endl;
}



int main() {
    int N, K;
    std::cin >> N >> K;
    
    std::vector<int> stoils;
    int x;
    while (std::cin >> x) {
        stoils.push_back(x);
    }
    
    solve(stoils, N, K);
}