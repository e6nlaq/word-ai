from janome.tokenizer import Tokenizer
import json
from random import randint
from os.path import isfile

t = Tokenizer()
path = "./demo.json"

print("================================")
print("学習モード")
print("\n`!end` で学習を終了")
print("================================")

if not isfile(path):
    with open(path, encoding="utf-8", mode="w") as f:
        f.write("{}")

with open(path, encoding="utf-8") as f:
    dat: dict[str, list[str]] = json.load(f)

while True:
    inp: str = input(">>> ")
    if inp != "!end":
        a = list(map(str, t.tokenize(inp, wakati=True)))
        dat.setdefault("!BEGIN", [])
        dat["!BEGIN"].append(a[0])
        for i in range(len(a)):
            dat.setdefault(a[i], [])
            if i != len(a) - 1:
                dat[a[i]].append(a[i + 1])
            else:
                dat[a[i]].append("!end")

        with open(path, mode="w", encoding="utf-8") as f:
            f.write(json.dumps(dat, indent=4, ensure_ascii=False))
    else:
        break

print("\n\n================================")
print("生成モード\n")
print("単語を入力するとその単語から生成")
print("空白で自動生成")
print("================================")

while True:
    make: str = input(">>> ")

    flag = False
    if make == "":
        make = "!BEGIN"
        flag = True

    ans: str = ""
    now: str = make

    if make != "!end":
        if not make in dat:
            print("そんな単語ないよ!")
        else:
            while now != "!end":
                ans += now
                now = dat[now][randint(0, len(dat[now]) - 1)]

            if flag:
                print(ans[6:])
            else:
                print(ans)
    else:
        print("じゃあね!")
        break
