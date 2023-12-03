import re
from collections import defaultdict

archivo=open("texto.txt","r")
def funcion1(archivo):
    lineas = archivo.read().splitlines()
    ans = 0
    for i, linea in enumerate(lineas):
        for m in re.finditer(r"\d+", linea):
            idxs = [(i, m.start() - 1), (i, m.end())]
            idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]
            idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]
            count = sum(0 <= a < len(lineas) and 0 <= b < len(lineas[a]) and lineas[a][b] != "." for a, b in idxs)
            if count > 0:
                ans += int(m.group())
    return ans
def funcion2(archivo):
    lineas = archivo.read().splitlines()
    adj = defaultdict(list)
    for i, linea in enumerate(lineas):
        for m in re.finditer(r"\d+", linea):
            idxs = [(i, m.start() - 1), (i, m.end())]
            idxs += [(i - 1, j) for j in range(m.start() - 1, m.end() + 1)]
            idxs += [(i + 1, j) for j in range(m.start() - 1, m.end() + 1)]
            for a, b in idxs:
                if 0 <= a < len(lineas) and 0 <= b < len(lineas[a]) and lineas[a][b] != ".":
                    adj[a, b].append(m.group())
    return sum(int(x[0]) * int(x[1]) for x in adj.values() if len(x) == 2)

print(funcion1(archivo))
print(funcion2(archivo))
