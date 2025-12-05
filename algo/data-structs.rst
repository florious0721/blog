数据结构
########

单调队列
--------

若向队尾追加新元素会打破队列的单调性时，
则不断将队尾弹出直到追加新元素也能满足单调性为止。

以维护一个单调递减的整数队列为例。

源：``1 2 -3 5 6 4 8``

#. ``1``，解释：``1`` 入队。
#. ``2``，解释：``2`` 大于 ``1``，入队。
#. ``-3``，解释：``-3`` 是最小的，队列清空后 ``-3`` 入队。
#. ``-3 5``，解释：`5` 大于 `-3`，入队。
#. ``-3 5 6``，解释：``6`` 大于 ``5``，入队。
#. ``-3 4``，解释：弹出 ``5``、``6`` 后 ``4`` 入队。
#. ``-3 4 8``，解释：``8`` 大于 ``4``，入队。

参见
____

`OI Wiki <https://oi-wiki.org/ds/monotonous-queue>`_

`洛谷专栏 <https://www.luogu.com.cn/article/1fiztcrj>`_

.. _binary_tree:

二叉树
------

数组表示
________

设根节点在数组中的索引为 ``root``，
那么左节点索引 ``l = 2 * root + 1``，
右节点索引 ``r = 2 * root + 2``。
然后采取一些方式表示叶节点或者空节点即可。

前中后序遍历
____________

这里的前、中、后指的是何时对当前节点进行操作。

对应地，前序遍历中第一项是当前的根，
第一项后面可被分为两个连续的块，
这两个块的第一项是当前节点的子节点，
特别地，当前项的下一项一定是当前节点的子节点。

中序遍历中无法直接确定根，
如果能找到根，那么根项前的所有项对应为左子树，
根项后的所有项对应为右子树。

后序遍历与前序遍历相反，最后一项是当前的根，
最后一项的前面可被分为两个连续的块，
这两个块的最后一项是当前节点的子节点，
特别地，最后一项的前一项一定是当前节点的子节点。

.. code:: cpp

  void preorder(int idx) {
    // do something to idx
    prefix(2 * idx + 1);
    prefix(2 * idx + 2);
  }

  void inorder(int idx) {
    infix(2 * idx + 1);
    // do something to idx
    infix(2 * idx + 2);
  }

  void postorder(int idx) {
    postfix(2 * idx + 1);
    postfix(2 * idx + 2);
    // do something to idx
  }

参见
____

`Hello 算法 <https://www.hello-algo.com/chapter_tree/binary_tree/>`_

`算法通关手册 <https://algo.itcharge.cn/05_tree/05_01_tree_basic/>`_

`知乎 <https://zhuanlan.zhihu.com/p/687719104>`_
