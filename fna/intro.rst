.. include:: ../refs.rst
.. include:: refs.rst

配置环境
########

约定
----

``游戏项目`` 指我们创建的新项目。

目录结构
--------

游戏项目和 FNA_、Nez_ 应该在同级目录下，
所以看起来应该是这样：

.. code::

  .
  ├── FNA
  ├── Nez
  ├── Game
  └── Game.sln

FNA_
----

请以 `官方文档 <fna-setup_>`_ 为主。

Linux_ 下的环境配置比较直接，安装 `.NET SDK <dotnet_>`_，
克隆 `FNA 仓库 <fna_>`_ 及其子模块（可以不克隆 FNA3D_）
之后就可以单独将其构建为 DLL 或将其作为项目引用添加到游戏项目中。

Nez_
----

遵循 `官方文档 <nez-fna-setup_>`_，
克隆仓库后作为项目引用添加到游戏项目中即可。
