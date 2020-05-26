<?php

$xml1="%3Capi%3E%0D%0A++++%3Crequest%3Eftp%3A%2F%2Flocalhost%3C%2Frequest%3E%0D%0A%3C%2Fapi%3E%0D%0A";
$xml = urldecode($xml1);
//echo $xml;
$reg = '/ftp:\/\/[\s\S]*\/\"/';
if (preg_match($reg, $xml, $match)) {
	$ip = explode('/', $match[0])[2];
	echo $ip;
	error_log("Connecting");
}

?>
