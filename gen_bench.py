import sys
def p(s): sys.stdout.write(s + '\n')
for i in range(8): p(f"INPUT(D{i})")
for i in range(8): p(f"INPUT(C{i})")
for i in range(8): p(f"OUTPUT(Z{i})")
g = 100
def xor2(a, b, out):
    global g
    p(f"N{g}=NAND({a},{b})")
    p(f"N{g+1}=NAND({a},N{g})")
    p(f"N{g+2}=NAND({b},N{g})")
    p(f"{out}=NAND(N{g+1},N{g+2})")
    g += 3
def xor_tree(inputs, out):
    global g
    curr = inputs[0]
    for idx in range(1, len(inputs)):
        nxt = out if idx == len(inputs)-1 else f"N{g}"
        if idx != len(inputs)-1: g += 1
        xor2(curr, inputs[idx], nxt)
        curr = nxt
xor_tree(["D7","D6","D0","C0","C6","C7"], "Z0")
xor_tree(["D6","D1","D0","C0","C1","C6"], "Z1")
xor_tree(["D6","D2","D1","D0","C0","C1","C2","C6"], "Z2")
xor_tree(["D7","D3","D2","D1","C1","C2","C3","C7"], "Z3")
xor_tree(["D4","D3","D2","C2","C3","C4"], "Z4")
xor_tree(["D5","D4","D3","C3","C4","C5"], "Z5")
xor_tree(["D6","D5","D4","C4","C5","C6"], "Z6")
xor_tree(["D7","D6","D5","C5","C6","C7"], "Z7")
