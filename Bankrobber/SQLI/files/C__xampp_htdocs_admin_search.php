<?php 
include('../link.php');

include('auth.php');

if(isset($_POST['term'])){
	$term = $_POST['term'];
	$stmt = $pdo->query("SELECT * from users WHERE id = '$term'") or die("There is a problem with your SQL syntax");
	echo "<table width='90%'><tr><th>ID</th><th>User</th></tr>";
	while($row = $stmt->fetch()){
		echo "
		<tr>
		    <td>$row[0]</td>
		    <td>$row[1]</td>
		 </tr>
		";
	}
	echo "</table>";
}
?>