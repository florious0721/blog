.. _LeetCode852: https://leetcode.cn/problems/peak-index-in-a-mountain-array/

题解记录
########

`山脉数组的峰顶索引 <LeetCode852_>`_
------------------------------------

二分查找，右边更高将区间右移，左边更高将区间左移，
否则缩小区间范围，直到
``arr[mid - 1] < arr[mid] && arr[mid] < arr[mid + 1]``。

.. code:: cpp

  class Solution {
  public:
      int peakIndexInMountainArray(vector<int>& arr) {
          int left = 0;
          int right = arr.size() - 1;
          int mid = (left + right) / 2;
          for (;;) {
              int leftmid = (left + mid) / 2;
              int rightmid = (mid + right) / 2;
              if (arr[leftmid] > arr[mid]) {
                  right = mid;
                  mid = leftmid;
              } else if (arr[rightmid] > arr[mid]) {
                  left = mid;
                  mid = rightmid;
              } else {
                  left = leftmid;
                  right = rightmid;
              }
              if (arr[mid - 1] < arr[mid] && arr[mid] > arr[mid + 1]) return mid;
          }
          return -1;
      }
  };
