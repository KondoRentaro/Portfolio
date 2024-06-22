<?php
  //データベース接続
  $pdo = new PDO("mysql:dbname=4rfij_blog;host=mysql1015.onamae.ne.jp", "4rfij_renkon200509", "Rentarou0509?");

  //postテーブルを新しい順でnoで検索
  $st = $pdo->query("SELECT * FROM post ORDER BY no DESC");

  //fetchで取得
  $posts = $st->fetchAll();

  //ひとつずつ記事をループしてその1つの記事に対応するコメントを格納、post_noで紐付け
  for ($i = 0; $i < count($posts); $i++) {
    $st = $pdo->query("SELECT * FROM comment WHERE post_no={$posts[$i]['no']} ORDER BY no DESC");

    //記事とコメントをpostsに格納
    $posts[$i]['comments'] = $st->fetchAll();
  }

  //t_index.php読み込み
  require 't_index.php';
?>
