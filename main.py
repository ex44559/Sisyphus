#!/usr/bin/env python3
from pexpect import pxssh
import pexpect


def reset_link() -> None:
    child = pexpect.spawn('ssh -CfnNT -R 2333:localhost:22 115.28.182.224 -p 2200 -l root')
    child.expect("root@115.28.182.224's password:")
    child.sendline("Sunbo220502")


def main() -> None:
    s = pxssh.pxssh()

    try:
        s.login("115.28.182.224", "root", "Sunbo220502", port="2200")
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)

    try:
        s.sendline('ssh 127.0.0.1 -p 2333 -l pi')
        s.expect("pi@127.0.0.1's password:")
        s.sendline('sunbo1')
    except pexpect.ExceptionPexpect as e:
        reset_link()
        print(e)

#s.logout()

if __name__ == '__main__':
    main()
