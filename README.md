# Python-Brainfuck-Visualiser
My Basic Brainfuck Visualiser is made in python as a project to see what i cloud do in python.
There are a few problems with how i wrote it and there are major problems with the code.
If you would like to patch any errors or problems with my code feel free.

Note: Don't use this to test your brainfuck code and expect it to work properly.

Known Problems:

1. I doesn't know how to ignore loops that aren't ever suppost to start.
```brainfuck
[+]
```

2. 2nd swtich is expecting an existing file
if hello.bf exists
```bash
py main.py hello.bf
```
it will output "Hello, World!"

if hello.bf doesn't exist or switch is not a file it will crash.
