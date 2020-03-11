import requests

'''
proxies ={
"http":"http://127.0.0.1:8080",
"https":"https://127.0.0.1:8080"
}
'''
'''
<!-- To Do:
			- Import Products
			- Link to new payment system
			- Enable SSL (Certificates location \\192.168.4.28\myfiles)
		<!-- Header -->
'''
proxy_server={
"http":"192.168.4.28"
}
url = "http://10.10.10.167/admin.php"
resp = requests.get(url,proxies=proxy_server)

print(resp.content)
