import os
cmd="netsh wlan show profiles | findstr Profile >> pass.txt "
os.system(cmd)
file=open("./pass.txt",'r+')
file2=open("./pass2.txt",'w')
file2.close()
file.readline()
print("Finding wifi HOSTS stored on your Device.....")
for i in file:
    a=i.split(":")[-1]
    ssid='"'+ a[1:-1] +'"'
    print("--->",a[1:-1])
    try:
        temp_cmd1="netsh wlan show profile name= " + ssid +" key=clear | findstr name >> pass2.txt"
        temp_cmd2="netsh wlan show profile name= " + ssid +" key=clear | findstr Key >> pass2.txt"
        os.system(temp_cmd1)
        os.system(temp_cmd2)
    except IndexError:
        print("Error while writing the password!!!")
file.close()
os.remove("./pass.txt")
print("Passwords are stored in the file pass2.txt")