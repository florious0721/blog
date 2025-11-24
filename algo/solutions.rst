题解记录
########

:leetcode:`852`
---------------

  给定一个长度为 ``n`` 的整数 **山脉** 数组 ``arr`` ，
  其中的值递增到一个 **峰值元素** 然后递减。
  返回峰值元素的下标。
  你必须设计并实现时间复杂度为 ``O(log(n))`` 的解决方案。

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

.. _luogu-p1440:

:luogu:`P1440`
--------------

  一个含有 *n* 项的数列，
  求出每一项前的 *m* 个数到它这个区间内的最小值。
  若前面的数不足 *m* 项则从第 *1* 个数开始，
  若前面没有数则输出 *0*。

暴力
====

最后一组数据 TLE。

.. code:: cpp

  #include <stdio.h>
  #include <algorithm>
  #include <vector>
  typedef unsigned long ulong;
  int main(void) {
      int n, m;
      ulong min = 0xffffffff;
      std::vector<ulong> v;
      scanf("%d%d", &n, &m);
      for (int i = 0; i < n; ++i) {
          ulong j;
          scanf("%lu", &j);
          v.push_back(j);
      }
      auto l = v.begin();
      auto r = l;
      puts("0");
      while (r - l < m) {
          min = *r < min ? *r : min;
          ++r;
          printf("%lu\n", min);
      }
      auto tail = v.end() - 1;
      while (r != tail) {
          if (*r < min) {
              min = *r;
          } else if (*l == min) {
              min = *std::min_element(l + 1, r + 1);
          }
          printf("%lu\n", min);
          ++r;
          ++l;
      }
      return 0;
  }

单调队列
========

.. code:: cpp

  #include <stdio.h>
  #include <algorithm>
  #include <deque>
  #include <vector>

  typedef unsigned long ulong;
  typedef struct {
      ulong val;
      long idx;
  } node;

  int main(void) {
      ulong n;
      long m;
      scanf("%lu%ld", &n, &m);
      std::deque<node> q;
      puts("0");
      for (long i = 0; i < n - 1; ++i) {
          ulong val;
          scanf("%lu", &val);
          while (!q.empty() && q.back().val > val) q.pop_back();
          q.push_back(node{val, i});
          if (!q.empty() && q.front().idx < i - (m - 1)) q.pop_front();
          printf("%lu\n", q.front().val);
      }
  }

.. _leetcode-239:

:leetcode:`239`
---------------

与 :ref:`luogu-p1440` 类似。

.. code:: cpp

  class Solution {
  public:
      vector<int> maxSlidingWindow(vector<int>& nums, int k) {
          vector<int> r;
          deque<int> q;
          int i = 0;
          for (; i < k; ++i) {
              while (!q.empty() && nums[q.back()] < nums[i]) q.pop_back();
              q.push_back(i);
          }
          r.push_back(nums[q.front()]);
          for (; i < nums.size(); ++i) {
              while (!q.empty() && nums[q.back()] < nums[i]) q.pop_back();
              q.push_back(i);
              if (!q.empty() && q.front() <= i - k) q.pop_front();
              r.push_back(nums[q.front()]);
          }
          return r;
      }
  };
