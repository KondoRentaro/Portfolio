<?php
// 認証情報を確認する関数
function authenticate() {
    // 設定するユーザー名とパスワード
    $username = 'renkon200509';
    $password = 'Kenta0120';

    // ユーザーが入力したユーザー名とパスワードを取得
    $enteredUsername = isset($_SERVER['PHP_AUTH_USER']) ? $_SERVER['PHP_AUTH_USER'] : '';
    $enteredPassword = isset($_SERVER['PHP_AUTH_PW']) ? $_SERVER['PHP_AUTH_PW'] : '';

    // 入力されたユーザー名とパスワードが正しいかチェック
    if ($enteredUsername !== $username || $enteredPassword !== $password) {
        // 認証が失敗した場合、認証ダイアログを表示し、401 Unauthorizedステータスを送信
        header('WWW-Authenticate: Basic realm="Restricted Area"');
        header('HTTP/1.0 401 Unauthorized');
        echo 'Authorization Required';
        exit;
    }
}

// 認証を実行
authenticate();?>

<?php   // ここから下には、認証成功後に実行したいコードを記述します
  $error = $title = $content = '';
  if (@$_POST['submit']) {
    $title = $_POST['title'];
    $content = $_POST['content'];
    if (!$title) $error .= 'タイトルがありません。<br>';
    if (mb_strlen($title) > 80) $error .= 'タイトルが長すぎます。<br>';
    if (!$content) $error .= '本文がありません。<br>';
    if (!$error) {
      $pdo = new PDO("mysql:dbname=4rfij_blog;host=mysql1015.onamae.ne.jp", "4rfij_renkon200509", "Rentarou0509?");
      $st = $pdo->query("INSERT INTO post(title,content) VALUES('$title','$content')");
      header('Location: index.php');
      exit();
    }
  }
  require 't_post.php';
?>