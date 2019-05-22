<?php
error_reporting(E_ALL & ~E_NOTICE);
class MyDB extends SQLite3 {
	function __construct() {
		$this->open('data.sqlite');
	}
}
function insert_record($db, $timestamp, $content){
	$stmt = $db->prepare('INSERT INTO "data" ("id", "timestamp", "content") VALUES (NULL, :timestamp, :content)');
	$stmt->bindParam(':timestamp', $timestamp);
	$stmt->bindParam(':content', $content);
	$result = $stmt->execute();
}
?>
