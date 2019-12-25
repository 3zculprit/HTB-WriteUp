<?php
$db_connection = pg_connect("host=localhost dbname=profiles user=profiles password=profiles");
$result = pg_query($db_connection, "SELECT * FROM profiles");
echo "$result";
while($row = mysql_fetch_assoc($result)) {
   $name = $row['username'];
   $passw =$row['password'];
   echo "$name";
   echo "$passw";	 	
}
?>
