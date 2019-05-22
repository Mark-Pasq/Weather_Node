<?php
include("global.php");
$db = new MyDB();
$result = $db->query('SELECT * FROM "data"');
?>
<!doctype html>
<html lang="en" class="h-100">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>DemoPage</title>
<link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/main.css" rel="stylesheet">
  </head>
  <body class="d-flex flex-column h-100">
<main role="main" class="flex-shrink-0">
  <div class="container">
    <h1 class="mt-5">Remote Sensor Data Demo</h1>
    <p>You can <a href="data.sqlite">download</a> our data if you want...</p>
<table class="table table-striped">
	<tr>
		<th>Time</th>
		<th>Data Content</th>
	</tr>
<?php 
while ($row = $result->fetchArray()){
?>
	<tr id="datarow-<?=$row['id']?>">
		<td><?=date('m/d/Y H:i:s', $row['timestamp']);?></td>
		<td><?=trim(str_replace("\n", '<br>', $row['content']));?></td>
	</tr>
<?php
}
?>
</table>
  </div>
</main>
</body>
</html>
