require 'winrm'

conn = WinRM::Connection.new(
  endpoint: 'http://10.10.10.149:5985/wsman',
  user: 'admin@support.htb',
  password: '4dD!5}x/re8]FBuZ',
  domain: 'SUPPORTDESK'	
)

command=""

conn.shell(:powershell) do |shell|
    until command == "exit\n" do
        print "PS > "
        command = gets        
        output = shell.run(command) do |stdout, stderr|
            STDOUT.print stdout
            STDERR.print stderr
        end
    end    
    puts "Exiting with code #{output.exitcode}"
end
