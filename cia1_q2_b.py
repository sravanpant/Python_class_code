def Fn(char: str = "*", cnt: int = 1):
    print(char * cnt)


Fn()
Fn("=")
Fn(cnt=3, char="$")
Fn(char="@")
Fn(cnt=3)
