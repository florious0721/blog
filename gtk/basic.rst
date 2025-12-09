.. include:: refs.rst

Gtk_
####

.. todo:: 将内容细化拆分。

ABC
---

现在的 GUI 框架一般都是提供一系列已经实现好的 **组件**，
应用开发者将这些组件用层次关系组合起来实现界面。

需要交互的组件则一般通过 `观察者模式 <design_pattern_observer_>`_
来给组件加上交互逻辑。

Gtk_ 是一套纯 C 实现的 GUI 框架，它以 GObject_ 作为底层的面向对象的框架。
在 Gtk_ 中，组件就是各种 :glink:`gtk4.class.Widget` 的派生类。
`观察者模式 <design_pattern_observer_>`_ 则通过信号机制实现，
我们可以使用 :glink:`gobject.func.signal_connect` 给组件加上某种信号产生时需要执行的代码。

添加依赖
--------

官方对 Meson_ 支持极佳，直接使用 ``dependency()`` 即可。

.. code:: meson

  gtk = dependency('gtk4')

:glink:`gtk4.class.Builder`
---------------------------

:glink:`gtk4.class.Builder` 通过从 xml（``.ui`` 文件，下文中称为 **界面文件**）读取组件层次结构来构建界面。

.. attention::

   **属性** 既可以指 xml 属性，也可以 GObject_ 的属性。
   本章中若无特别说明，则指 GObject_ 的属性，否则会使用 ``xml 属性`` 明确指出。

根节点一定是 ``<interface>``，
每个 ``<object>`` 对应一个 :glink:`gobject.class.Object`，
通过 ``class`` xml 属性来指定其类型。
在 ``<object>`` 内通过 ``<property>`` 节点来设置类的属性，
通过 ``<child>`` 来添加子组件。
有些组件有不同种类的子组件，这时可以通过 ``type`` xml 属性来指定种类。

对于一些特殊的组件（如 :glink:`gtk4.class.Notebook`）请查阅 `官方文档 <gtk_>`_，
本文也记录了一些在 GtkBuilder_ 中用过的特殊组件。

:glink:`gtk4.class.ListView`
____________________________

建议使用 :glink:`gtk4.class.SignalListItemFactory`。
:glink:`gtk4.class.BuilderListItemFactory` 的功能有限，
主要用于列表项只读的情况（因为在 ``.ui`` 文件中绑信号还是比较麻烦的）。

.. code:: xml

  <object id='upcomingAlbums' class='GtkListView'>

    <property name='model'><object class='GtkNoSelection'>
      <property name='model'><object id='albumList' class='GListStore'>
        <property name='item-type'>VocagtkAlbum</property>
      </object></property>
    </object></property>

    <property name='factory'>
      <object id='albumFactory' class='GtkSignalListItemFactory'/>
    </property>
  </object>

:glink:`gtk4.class.Notebook`
____________________________

指定 xml 属性 ``type='tab'`` 可以将子组件设置在标签页的标签部分。

.. code:: xml

  <object class='GtkNotebook'>
    <property name='tab-pos'>0</property>

    <child type='tab'><object class='GtkImage'/></child>
    <child><object class='GtkBox'/></child>
  </object>
