import winrm

session = winrm.Session("10.10.10.149",auth=("SUPPORTDESK\Chase","Q4)sJu\Y8qz*A3?d"),transport="negotiate")
result = session.run_cmd('ipconfig', ['/all'])

print (result)
