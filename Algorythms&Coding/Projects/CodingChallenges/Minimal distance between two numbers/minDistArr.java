package practice;

public class minDistArr {

	public int minDist(int[] arr, int n, int x, int y) {
		int lastX = -1;
		int lastY = -1;
		int dist = n + 1;
		int distTemp;

		for (int i = 0; i < n; i++) {
			if (arr[i] == x) {
				lastX = i;
				if (lastY >= 0) {
					distTemp = lastX - lastY;
					if (distTemp < dist) {
						dist = distTemp;
					}
				}
			}

			if (arr[i] == y) {
				lastY = i;
				if (lastX >= 0) {
					distTemp = lastY - lastX;
					if (distTemp < dist) {
						dist = distTemp;
					}
				}
			}
		}
		if (dist > n) {
			return -1;

		} else {
			return dist;
		}

	}

}
