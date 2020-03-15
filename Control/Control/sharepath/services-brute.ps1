$reader = [System.IO.File]::OpenText("services-list.txt")
while($null -ne ($line = $reader.ReadLine())) {
	$arrService = sc.exe qc $line
	if ($arrService -contains "Access is denied."){
}elseif($arrService -contains "The specified service does not exist as an installed service."){
}else
{	$arrService | Format-Table
}
}
