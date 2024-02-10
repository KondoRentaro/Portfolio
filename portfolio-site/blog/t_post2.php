<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>記事投稿 | Special Blog</title>
<link rel="stylesheet" href="blog.css">
</head>
<body>
<?php echo isset($_GET['id']) ? htmlspecialchars($_GET['id']) : ''; ?>
<form method="post" action="f_post.php?id=<?php echo $_GET['id']; ?>">
  <div class="post">
    <h2>記事投稿</h2>
    <p>題名</p>
    <p><input type="text" name="title" size="40" value="<?php echo htmlspecialchars($title); ?>"></p>
    <p>本文</p>
    <p><textarea name="content" rows="8" cols="40"><?php echo htmlspecialchars($content); ?></textarea></p>
    <p><input name="submit" type="submit" value="修正"></p>
    <p><?php echo $error; ?></p>
  </div>
</form>
</body>
</html>
