<?php
// データベース接続
$db_password = getenv("MYSQL_PASSWORD");
$pdo = new PDO("mysql:dbname=blog;host=localhost", "root", $db_password);

// 投稿のIDが指定されていない場合はエラーを表示
if (!isset($_GET['no']) || empty($_GET['no'])) {
    echo "IDが指定されていません。";
    exit();
}

// 投稿のIDに対応するデータを取得
$st = $pdo->prepare("SELECT * FROM post WHERE no=?");
$st->execute([$_GET['no']]);
$post = $st->fetch(PDO::FETCH_ASSOC);

// POSTリクエストがあった場合は更新を行う
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $title = $_POST['title'];
    $content = $_POST['content'];
    
    // バリデーション
    $error = '';
    if (!$title) $error .= 'タイトルがありません。<br>';
    if (mb_strlen($title) > 80) $error .= 'タイトルが長すぎます。<br>';
    if (!$content) $error .= '本文がありません。<br>';
    
    // エラーがない場合、データベースを更新
    if (!$error) {
        $st = $pdo->prepare("UPDATE post SET title=?, content=? WHERE no=?");
        $st->execute([$title, $content, $_GET['no']]);
        
        // トップページへリダイレクト
        header('Location: index.php');
        exit();
    }
}
?>

<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>記事編集 | Special Blog</title>
<link rel="stylesheet" href="blog.css">
</head>
<body>
<h1>記事編集</h1>
<form method="post" action="">
  <div class="post">
    <p>タイトル</p>
    <p><input type="text" name="title" size="40" value="<?php echo htmlspecialchars($post['title']); ?>"></p>
    <p>本文</p>
    <p><textarea name="content" rows="8" cols="40"><?php echo htmlspecialchars($post['content']); ?></textarea></p>
    <p><input name="submit" type="submit" value="更新"></p>
    <p><?php if(isset($error)) echo $error; ?></p>
  </div>
</form>
</body>
</html>
