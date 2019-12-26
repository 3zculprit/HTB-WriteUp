from subprocess import PIPE, Popen
import subprocess
import sys

def cmdline(command):
    proc = subprocess.Popen(str(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return err

def main():
    words = [line.strip() for line in open('/usr/share/wordlists/rockyou.txt')]
    print("\n")
    count=0

    for w in words:
        strcmd = "openssl rsa -in ~/Desktop/HTB/boxes/Registry/id_rsa -out ~/Desktop/HTB/boxes/Registry/id_rsa_dec -passin pass:"+w
        print (strcmd)
	res=cmdline(strcmd)
	print (res)
        if res.startswith("writing"):
                print("\nThe key is: "+w)
                sys.exit()
        print(str(count)+"/"+str(w))
        count=count+1
    print("\n")

if __name__ == '__main__':
    main()
