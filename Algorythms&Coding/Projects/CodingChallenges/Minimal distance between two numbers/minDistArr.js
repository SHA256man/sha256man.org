class Solution {
  minDist(a, n, x, y) {
    let lastx = -1
    let lasty = -1
    let dist = n + 1

    for (let i = 0; i < n; i++) {
      if (a[i] == x) {
        lastx = i;
        if (lasty >= 0) {
          let dist2 = lastx - lasty;
          if (dist2 < dist) dist = dist2;
        }
      }
      if (a[i] == y) {
        lasty = i
        if (lastx >= 0) {
          let dist2 = lasty - lastx;
          if (dist2 < dist) dist = dist2;
        }
      }
    }

    if (dist > n) return -1
    return dist
  }
}