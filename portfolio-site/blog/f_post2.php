<?php
$error = $title = $content = '';

// フォームが送信された場合
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $title = $_POST['title'];
    $content = $_POST['content'];
    
    // バリデーション
    if (!$title) $error .= 'タイトルがありません。<br>';
    if (mb_strlen($title) > 80) $error .= 'タイトルが長すぎます。<br>';
    if (!$content) $error .= '本文がありません。<br>';
    
    // エラーがない場合、データベースを更新
    if (!$error) {
        // データベース接続
        $db_password = getenv("MYSQL_PASSWORD");
        $pdo = new PDO("mysql:dbname=blog;host=localhost", "root", $db_password);
        
        // 更新クエリの実行
        $st = $pdo->prepare("UPDATE post SET title=?, content=? WHERE no=?");
        $st->execute([$title, $content, $_GET['id']]);
        
        // トップページへリダイレクト
        header('Location: index.php');
        exit();
    }
} else {
    // GETリクエストの場合、記事の情報を取得してフォームに表示
    $db_password = getenv("MYSQL_PASSWORD");
    $pdo = new PDO("mysql:dbname=blog;host=localhost", "root", $db_password);
    $st = $pdo->prepare("SELECT * FROM post WHERE no=?");
    $st->execute([$_GET['id']]);
    $row = $st->fetch(PDO::FETCH_ASSOC);
    $title = $row['title'];
    $content = $row['content'];
}

// フォームテンプレートの読み込み
require 't_post.php';
?>



<?php
$error = $title = $content = '';

// フォームが送信された場合
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $title = $_POST['title'];
    $content = $_POST['content'];
    
    // バリデーション
    if (!$title) $error .= 'タイトルがありません。<br>';
    if (mb_strlen($title) > 80) $error .= 'タイトルが長すぎます。<br>';
    if (!$content) $error .= '本文がありません。<br>';
    
    // エラーがない場合、データベースを更新
    if (!$error) {
        // データベース接続
        $db_password = getenv("MYSQL_PASSWORD");
        $pdo = new PDO("mysql:dbname=blog;host=localhost", "root", $db_password);
        
        // 更新クエリの実行
        $st = $pdo->prepare("UPDATE post SET title=?, content=? WHERE no=?");
        $st->execute([$title, $content, $_GET['id']]);
        
        // トップページへリダイレクト
        header('Location: index.php');
        exit();
    }
} else {
    // GETリクエストの場合、記事の情報を取得してフォームに表示
    $db_password = getenv("MYSQL_PASSWORD");
    $pdo = new PDO("mysql:dbname=blog;host=localhost", "root", $db_password);
    $st = $pdo->prepare("SELECT * FROM post WHERE no=?");
    $st->execute([$_GET['id']]);
    $row = $st->fetch(PDO::FETCH_ASSOC);
    $title = $row['title'];
    $content = $row['content'];
}

// フォームテンプレートの読み込み
require 't_post.php';
?>