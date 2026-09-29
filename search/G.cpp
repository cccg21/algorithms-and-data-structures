#include <iostream> 
#include <vector>
#include <algorithm>

void solve(std::vector<int> &verevki, int N, int K) {
    int max = 0;
    int answer = 0;
    
    for (int i = 0; i < verevki.size(); i++) {
        if (max < verevki[i]) {
            max = verevki[i];
        }
    }

    int low = 1; int high = max;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        
        int count = 0;
        for (int i = 0; i < verevki.size(); i++) {
            count += verevki[i] / mid;
        }

        if (count >= K) {
            answer = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    
    if (answer == 0) {
        std::cout << 0 << std::endl;
    } else {
        std::cout << answer << std::endl;
    }
}

int main () {
    int N, K;
    std::cin >> N >> K;
    std::vector<int> verevki(N);
    int x;

    for (int i = 0; i < verevki.size(); i++) {
        std::cin >> x;
        verevki[i] = x;
    }

    solve(verevki, N, K);
}