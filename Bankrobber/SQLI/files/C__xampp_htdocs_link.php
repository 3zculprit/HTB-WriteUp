<?php
$user = 'root';
$pass = 'Welkom1!';
$dsn = "mysql:host=127.0.0.1;dbname=bankrobber;";

$pdo = new PDO($dsn,$user,$pass);

function echoBalance($pdo){
	$pdo = $pdo;
	if(isset($_COOKIE['id'])){
		$stmt = $pdo->prepare("SELECT amount FROM balance where userId = ?");
		$stmt->execute([$_COOKIE['id']]);

		while($row = $stmt->fetch()){
			return $row[0];
		}
	}
}
?>