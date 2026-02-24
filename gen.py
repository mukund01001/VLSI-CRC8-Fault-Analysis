with open("crc8.bench", "w") as f:
    for i in range(8): f.write(f"INPUT(D{i})\n")
    for i in range(8): f.write(f"INPUT(C{i})\n")
    f.write("\n")
    for i in range(8): f.write(f"OUTPUT(Z{i})\n")
    f.write("\n")

    gate_counter = 1
    def make_xor(a, b, out_name=None):
        global gate_counter
        n1 = f"N{gate_counter}"; gate_counter += 1
        n2 = f"N{gate_counter}"; gate_counter += 1
        n3 = f"N{gate_counter}"; gate_counter += 1
        out = out_name if out_name else f"N{gate_counter}"
        if not out_name: gate_counter += 1
        f.write(f"{n1} = NAND({a}, {b})\n")
        f.write(f"{n2} = NAND({a}, {n1})\n")
        f.write(f"{n3} = NAND({b}, {n1})\n")
        f.write(f"{out} = NAND({n2}, {n3})\n")
        return out

    def xor_list(inputs, final_out):
        current = inputs[0]
        for i in range(1, len(inputs)):
            if i == len(inputs) - 1:
                make_xor(current, inputs[i], final_out)
            else:
                current = make_xor(current, inputs[i])
        f.write("\n")

    xor_list(["D7", "D6", "D0", "C0", "C6", "C7"], "Z0")
    xor_list(["D6", "D1", "D0", "C0", "C1", "C6"], "Z1")
    xor_list(["D6", "D2", "D1", "D0", "C0", "C1", "C2", "C6"], "Z2")
    xor_list(["D7", "D3", "D2", "D1", "C1", "C2", "C3", "C7"], "Z3")
    xor_list(["D4", "D3", "D2", "C2", "C3", "C4"], "Z4")
    xor_list(["D5", "D4", "D3", "C3", "C4", "C5"], "Z5")
    xor_list(["D6", "D5", "D4", "C4", "C5", "C6"], "Z6")
    xor_list(["D7", "D6", "D5", "C5", "C6", "C7"], "Z7")
