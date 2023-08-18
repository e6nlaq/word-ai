from janome.tokenizer import Tokenizer
import json
from random import randint

t = Tokenizer()

print("================================")
print("ようこそ!AIもどきへ!")
print("\n`!end` で学習を終了するよ!")
print("================================")

with open("./data.json", encoding="utf-8") as f:
    dat: dict[str, list[str]] = json.load(f)

while True:
    inp: str = input(">>> ")
    if inp != "!end":
        a = list(t.tokenize(inp, wakati=True))
        for i in range(len(a)):
            dat.setdefault(a[i], [])
            if i != len(a) - 1:
                dat[a[i]].append(a[i + 1])
            else:
                dat[a[i]].append("!end")

        with open("./data.json", mode="w", encoding="utf-8") as f:
            f.write(json.dumps(dat, indent=4, ensure_ascii=False))
    else:
        break

print("================================")
print("試してみよう!")
print("================================")

while True:
    inp: str = input(">>> ")
    ans: str = ""
    now: str = inp
    if inp != "!end":
        if not inp in dat:
            print("んなもんねえよ!出直せ!")
        else:
            while now != "!end":
                ans += now
                now = dat[now][randint(0, len(dat[now]) - 1)]
            print(ans)
    else:
        print("See you!")
        break
