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

:luogu:`P1440`
--------------

  一个含有 *n* 项的数列，
  求出每一项前的 *m* 个数到它这个区间内的最小值。
  若前面的数不足 *m* 项则从第 *1* 个数开始，
  若前面没有数则输出 *0*。

暴力
____

我们可以记录下当前窗口内的最小值，
接着考虑窗口内的数、即将出窗口的数、即将进窗口的数，
若进的数比当前最小值更小，更新最小值，
若出的数是当前的最小值，那么重新求窗口内的最小值。

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
________

对上面的方法进一步优化，关键在于剔除那些不可能成为窗口内最小值的数。
我们用单调队列存储这个滑动窗口，
对于一个即将进入窗口的数 :math:`a_i`，
只要它在窗口内，那么比它大的数都无法成为最小值，
所以可以把队列里比它大的数都弹出，
这样我们就可以确保队列是单调递增的，
队头则为当前窗口内的最小值，
接着再在每次移动窗口时把超过窗口范围的数弹出即可。

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

:leetcode:`239`
---------------

  给你一个整数数组 ``nums``，
  有一个大小为 ``k`` 的滑动窗口从数组的最左侧移动到数组的最右侧。
  你只可以看到在滑动窗口内的 ``k`` 个数字。滑动窗口每次只向右移动一位。

  返回 *滑动窗口中的最大值*。

与 :ref:`lgp1440` 类似，反过来求最大值即可。

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

:luogu:`P1714`
--------------

  形式化地，在数列 :math:`\lbrace p_n \rbrace` 中，
  找出一个字段 :math:`[l, r](r-l + 1 \leq m)`，
  最大化 :math:`\sum\limits_{i=l}^rp_i`。

这题就是在 :ref:`max_interval_sum` 的基础上限制了区间长度。
因为 :ref:`max_interval_sum` 需要频繁计算区间值，
所以用 :ref:`prefix_sum` 优化，
然后再用单调队列维护一个单调递增的前缀和进一步优化。

这题要注意弹出头、求值、弹出尾并插入新值的顺序。

.. code:: cpp

  #include <limits.h>
  #include <stdio.h>
  #include <queue>
  #include <vector>

  int main(void) {
      std::deque<long> q;
      long sumv[500000+0x100] = {0};

      long n, m;
      scanf("%ld%ld", &n, &m);

      long cur_sum = 0;
      for (long i = 1; i <= n; ++i) {
          long j = 0;
          scanf("%ld", &j);
          cur_sum += j;
          sumv[i] = cur_sum;
      }

      long ans = LONG_MIN;
      q.push_back(0);
      for (long i = 1; i <= n; ++i) {
          while (!q.empty() && i - q.front() > m) q.pop_front();
          long new_ans = sumv[i] - sumv[q.front()];
          ans = new_ans > ans ? new_ans : ans;
          while (!q.empty() && sumv[q.back()] >= sumv[i]) q.pop_back();
          q.push_back(i);
      }

      printf("%ld\n", ans);
      return 0;
  }

:luogu:`P2032`
--------------

同 :ref:`lc239` 略。
