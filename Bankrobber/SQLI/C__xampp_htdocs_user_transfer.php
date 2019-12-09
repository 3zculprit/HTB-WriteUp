<?php
error_reporting(0);
include('../link.php');
include('auth.php');

$fromId  = is_numeric($_POST['fromId']) ? $_POST['fromId'] : 1; 
$toId 	 = is_numeric($_POST['toId'])   ? $_POST['toId'] : 1;
$amount  = is_numeric($_POST['amount']) ? $_POST['amount'] : 1;
$comment = urlencode($_POST['comment']);

$stmt = $pdo->prepare("INSERT INTO hold (userIdFrom,userIdTo,amount,comment) VALUES (?,?,?,?)");
$stmt->execute([$fromId,$toId,$amount,$comment]);
?>