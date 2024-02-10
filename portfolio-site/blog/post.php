<?php
  $error = $title = $content = '';
  if (@$_POST['submit']) {
    $title = $_POST['title'];
    $content = $_POST['content'];
    if (!$title) $error .= 'タイトルがありません。<br>';
    if (mb_strlen($title) > 80) $error .= 'タイトルが長すぎます。<br>';
    if (!$content) $error .= '本文がありません。<br>';
    if (!$error) {
      $db_password = getenv("MYSQL_PASSWORD");
      $pdo = new PDO("mysql:dbname=blog;host=localhost", "root", $db_password);
      $st = $pdo->query("INSERT INTO post(title,content) VALUES('$title','$content')");
      header('Location: index.php');
      exit();
    }
  }
  require 't_post.php';
?>