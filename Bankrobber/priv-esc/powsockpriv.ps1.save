$Ipaddress= "127.0.0.1"
$Port= "910"
$tcp = New-Object System.Net.Sockets.TcpClient($Ipaddress,$Port)
$tcpstream = $tcp.GetStream()
$reader = New-Object System.IO.StreamReader($tcpStream)
$writer = New-Object System.IO.StreamWriter($tcpStream)
$writer.AutoFlush = $true

while ($tcp.Connected)
{       
write-host ([char]$reader.Read()) -NoNewline
while(($reader.Peek() -ne -1) -or ($tcp.Available)){        
    write-host ([char]$reader.Read()) -NoNewline
}
if ($tcp.Connected)
{
    Write-Host -NoNewline ""
    $command = Read-Host

    if ($command -eq "escape")
    {
        break
    }

}     
}
$reader.Close()
$writer.Close()
$tcp.Close()
