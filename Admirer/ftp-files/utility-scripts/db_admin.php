<?php
  $servername = "localhost";
  $username = "waldo";
  $password = "Wh3r3_1s_w4ld0?";
  $db = "admirerdb";
  $protocol = "tcp";	
  // Create connection
  $conn = new mysqli($servername, $username, $password,$db,$protocol);

  // Check connection
  if ($conn->connect_error) {
      die("Connection failed: " . $conn->connect_error);
  }
  echo "Connected successfully";


  // TODO: Finish implementing this or find a better open source alternative
?>
