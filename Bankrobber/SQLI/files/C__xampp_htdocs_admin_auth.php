<?php
error_reporting(0);

$username = base64_decode(urldecode($_COOKIE['username']));
$password = base64_decode(urldecode($_COOKIE['password']));

if($username != "admin" || $password != "Hopelessromantic"){
	die("You're not authorized to view this page");
}
?>