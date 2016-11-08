#!/usr/bin/env python3
from pexpect import pxssh


def main() -> None:
    try:
        s = pxssh.pxssh()
        s.login("115.28.182.224", "root", "Sunbo220502", port="2200")
        s.sendline('who')
        s.prompt()
        print(s.before)
        s.logout()
    except pxssh.ExceptionPxssh as e:
        print("pxssh failed on login.")
        print(e)

if __name__ == '__main__':
    main()
