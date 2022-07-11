#include <iostream>

class Solution {
public:
  int minDist(int a[], int n, int x, int y) {
    int dist = n + 1;
    int dist2;
    int lastx = -1;
    int lasty = -1;

    for (int i = 0; i < n; i++) {
      if (*(a + i) == x) {
        lastx = i;
        if (lasty > -1) {
          dist2 = lastx - lasty;
          if (dist2 < dist)
            dist = dist2;
        }
      }
      if (*(a + i) == y) {
        lasty = i;
        if (lastx > -1) {
          dist2 = lasty - lastx;
          if (dist2 < dist)
            dist = dist2;
        }
      }
    }

    if (dist > n)
      dist = -1;
    return dist;
  }
};

int main() {
  int a[9] = {1, 6, 7, 9, 1, 3, 8, 4, 5};
  int n = 9;
  int x = 1;
  int y = 8;

  Solution obj;

  std::cout << obj.minDist(a, n, x, y) << "\n";

  return 0;
}
