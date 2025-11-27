Sql
###

建表
----

.. code:: sql

  CREATE TABLE IF NOT EXISTS albums(
    id INTEGER PRIMARY KEY,
    name TEXT,
    artist TEXT,
  );

关联表（多对多）
----------------

.. code:: sql

  CREATE TABLE IF NOT EXISTS tracks(
    id INTEGER PRIMARY KEY,
    name TEXT,
    artist TEXT,
  );

  CREATE TABLE IF NOT EXISTS album_track_links(
    album INTEGER,
    track INTEGER,
    FOREIGN KEY(album) REFERENCES albums(id),
    FOREIGN KEY(track) REFERENCES tracks(id)
  );

增
--

.. code:: sql

  INSERT INTO
    albums (id, name, artist)
    VALUES (33845, '熱異常', 'いよわ feat. 足立レイ');

查
--

.. code:: sql

  SELECT a.name
    FROM albums AS a
    JOIN album_track_links AS atl ON atl.album = a.id
    JOIN tracks AS t ON t.id = atl.track
    WHERE name='熱異常'
    ORDER BY name ASC;

``AS`` 可以省略。
通过专辑名查询专辑的所有音轨。
