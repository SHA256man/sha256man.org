# You are given an array A, of N elements. Find minimum index based distance
# between two elements of the array, x and y.

# Example:
# Input:
# N = 4
# A[] = {1,2,3,2}
# x = 1, y = 2
# Output: 1
# Explanation: x = 1 and y = 2. There are
# two distances between x and y, which are
# 1 and 3 out of which the least is 1.
#
# Constraints:
# 1 <= N <= 10^5
# 0 <= A[i], x, y <= 10^5


class Solution:
    @staticmethod
    def minDist(arr: list, n: int, x: int, y: int) -> int:
        lastX = -1
        lastY = -1
        # var for min dist initalized as upper bound
        dist = n + 1

        # loop only once throuh the arr for O(n).
        for i in range(n):
            if (arr[i] == x):
                # mark the last index of apperance of x
                lastX = i
                if (lastY >= 0):
                    # compute new dist
                    distTemp = lastX - lastY
                    if distTemp < dist:
                        # set new dist if it is smaller than current min.
                        dist = distTemp
            if (arr[i] == y):
                # mark the last index of apperance of y
                lastY = i
                if (lastX >= 0):
                    # compute new dist
                    distTemp = lastY - lastX
                    if distTemp < dist:
                        # set new dist if it is smaller than current min.
                        dist = distTemp
        # return -1 in case x & y are not in arr
        if (dist > n):
            return -1
        else:
            return dist


def main():
    a = [98, 78, 10, 12, 59, 37, 45, 18, 1, 56, 37, 14, 3, 32, 85, 10,
         69, 89, 29, 93, 44, 16, 26, 13, 50, 75, 79, 21, 20, 33, 55, 17,
         63, 64, 80, 21, 52, 24, 90, 52, 80, 26, 18, 34, 57, 2, 95, 25, 42,
         23, 17, 85, 39, 94, 50, 40, 21, 28, 12, 40, 61, 67, 9, 23, 30, 88,
         95, 34, 64, 85, 85, 95, 62, 54, 28, 19, 55, 22, 95, 49, 97, 64, 33]
    sol = Solution()
    print(sol.minDist(a, 83, 34, 56))


if __name__ == '__main__':
    main()
