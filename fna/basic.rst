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

可以使用泛型方法

* :func:`Content.Load<T>(string path)`

也可以使用具体方法

* :func:`Content.LoadTexture(string path)`
* :func:`Content.LoadTiledMap(string path)`

.. attention:: ``path`` 是相对于游戏所在目录的路径。


:class:`Nez.Textures.Sprite` 是 :class:`Texture2D` 的封装，
它引用源材质并提供一个切片矩形，
用于指示材质的哪一部分是一张单独的精灵图。

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
* :class:`SpriteAnimator`
* :class:`TiledMapRenderer`

* :class:`BoxCollider`
* :class:`TiledMapMover`

  .. attention::

     :class:`ArcadeRigidbody` 没有提供完整的物理模拟，
     只提供了一些角色控制的常见物理功能。

     和 Unity_ 不同，组件基类是没有 :func:`Update()` 的，
     要实现接口 :interface:`IUpdatable` 才会每帧进行更新。
