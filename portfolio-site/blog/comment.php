<?php

  //初期化
  $post_no = $error = $name = $content = '';

  if (@$_POST['submit']) {

    //タグ取り除いてる
    $post_no = strip_tags($_POST['post_no']);
    $name = htmlspecialchars($_POST['name'], ENT_QUOTES, 'UTF-8');
    $content = htmlspecialchars($_POST['content'], ENT_QUOTES, 'UTF-8');

    //エラー処理
    if (!$name) $error .= '名前がありません。<br>';
    if (!$content) $error .= 'コメントがありません。<br>';

    // 文字数制限を設定、mbはバイト数ではなく文字数
    if (mb_strlen($name) > 50) $error .= '名前は50文字以下で入力してください。<br>';

    if (mb_strlen($content) > 1000) $error .= 'コメントは1000文字以下で入力してください。<br>';

    if (!$error) {
      $pdo = new PDO("mysql:dbname=4rfij_blog;host=mysql1015.onamae.ne.jp", "4rfij_renkon200509", "Rentarou0509?");
      $st = $pdo->prepare("INSERT INTO comment(post_no,name,content) VALUES(?,?,?)");
      $st->execute(array($post_no, $name, $content));

      //投稿したらindexへ
      header('Location: index.php');
      exit();
    }
  } else {
    $post_no = strip_tags($_GET['no']);
  }
  require 't_comment.php';
?>