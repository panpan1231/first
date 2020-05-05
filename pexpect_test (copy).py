import pexpect
import os 
os.chdir('/home/jlo/Desktop')

def ssh_conect():
    try:
        p = pexpect.spawn('ssh root@10.100.43.132',encoding='utf-8')
        p.expect('password:')
        p.sendline('1111')
        fout = open ('logfile.txt', "w+")
        p.logfile = fout
        
        p.expect('~]# ')
        p.sendline('top -n 1')

        p.expect('~]# ')
        p.sendline('top -n 1')

        p.expect('~]# ')
        p.sendline('top -n 1')
   
        p.expect('~]# ')
        p.sendline('exit')

        p.expect(pexpect.EOF)
        
    except pexpect.EOF:
        print('EOF')
    except pexpect.TIMEOUT:
        print('TIMEOUT')
        ssh_conect()
    else:
        fout.close()
ssh_conect()
