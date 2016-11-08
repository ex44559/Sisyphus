#!/usr/bin/env python3
from pexpect import pxssh
import pexpect


def reset_link() -> None:
    child = pexpect.spawn('ssh -CfnNT -R 2333:localhost:22 115.28.182.224 -p 2200 -l root')
    child.expect("root@115.28.182.224's password:")
    child.sendline("Sunbo220502")


def main() -> None:
    try:
        s = pxssh.pxssh()
        s.login("115.28.182.224", "root", "Sunbo220502", port="2333")
        s.sendline('who')
        s.prompt()
        print(s.before)
        s.logout()
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)

if __name__ == '__main__':
    main()
