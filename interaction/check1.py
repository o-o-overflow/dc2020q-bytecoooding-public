#!/usr/bin/env python3

import sys
import re

from pwn import *
context.log_level = 'debug'

def main():

    host = sys.argv[1]
    port = int(sys.argv[2])

    solutions = [('Bytecode.class', 'jvm', 8),
                 ('solution.cpython-36.pyc', 'python3', 4),
                 ('solution.pyc', 'python2', 4),
                 ('ruby_solution', 'ruby', 12),
                 ('lua_bytecode_solution', 'lua', 18),
                 ('solution.jsc', 'nodejs', 0),
                 ('solution.cmo', 'ocaml', 12),
                 ('solution.elisp', 'elisp', 0),
    ]

    for (filename, platform, preamble) in reversed(solutions):
        conn = remote(host, port)
        conn.recvuntil('Bytecode: ')

        with open(f"solutions/{filename}", 'rb') as f:
            f.seek(preamble)
            conn.send(f.read())
        conn.recvuntil('> ')

        conn.sendline(platform)
        conn.sendline("quit")

        result = conn.recvuntil("Not quite there")

        r = re.search(b'You got (\d+) correct', result)
        assert(r)
        assert(int(r.group(1)) == 1)
    
    sys.exit(0)


if __name__ == '__main__':
    main()
