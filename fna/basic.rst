.. include:: refs.rst

基础
####

游戏类
------

.. code:: C#

  using Nez;

  class NewGame: Core {
      public static int Main(string[] args) {
          using (NewGame g = new NewGame()) g.Run();
          return 0;
      }

      protected override void Initialize() {
          base.Initialize();
          Scene = new MainScene();
      }
  }

游戏类继承 :class:`Nez.Core` 重载 :func:`Nez.Core.Initialize()`
设置初始场景并在 :func:`Main()` 中调用 :func:`Run()` 运行游戏。

资源管理
--------

* :func:`Content.Load<T>(string path)` 从 ``Content`` 中加载资源。

  :func:`Content.Load<Texture2D>(string path)` 加载材质。

:class:`Nez.Textures.Sprite` 是 :class:`Texture2D` 的封装，
它引用源材质并提供一个切片矩形用于指示材质的哪一部分是一张
单独的精灵图。

ECS
---

Nez_ 的 ECS 和 Unity_ 的很像。

* :func:`Scene.CreateEntity(string name)` 创建一个 :class:`Entity`。
* :func:`Entity.AddComponent(Component c)` 给 :class:`Entity` 添加组件。
* :func:`Entity.SetParent(Entity e)` 设置父 :class:`Entity`。

重要的组件
----------

* :class:`Transform`
* :class:`Camera`
* :class:`SpriteRenderer`

  :class:`TiledSpriteRenderer`
* :class:`BoxCollider`
* :class:`ArcadeRigidbody`

  .. attention::

     :class:`ArcadeRigidbody` 没有提供完整的物理模拟，
     只提供了一些角色控制的常见物理功能。

组件基类是没有 :func:`Update()` 的，
要实现接口 :interface:`IUpdatable` 才会每帧进行更新。

渲染
----

:interface:`IRenderable` 和 :class:`SpriteBatch` 或 :class:`Batcher`
是理解渲染部分的核心。

FNA_ 中没有 PPU 的概念，默认直接以像素为单位，也无法单独为 :class:`Texture2D` 或 Nez_ 中的 :class:`Sprite` 设置
缩放，一个良好实践是将 :class:`SpriteRenderer` 放到子 :class:`Entity` 上，在 Unity_ 中也是常见操作。
这里我借助 PPU 的概念来帮助计算应该如何设置缩放的值。

.. todo:: 补充渲染部分。
