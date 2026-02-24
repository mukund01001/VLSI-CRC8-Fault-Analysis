# ATPG and Fault Coverage Analysis of a CRC-8 Integrity Module

## 📌 Project Overview
This project implements a purely combinational, parallel 8-bit Cyclic Redundancy Check (CRC) generator and evaluates its testability using Automatic Test Pattern Generation (ATPG). 

By mathematically unrolling 8 clock cycles of LFSR shifts into a single combinational XOR-tree, the module calculates the remainder instantaneously. A core focus of this project was analyzing structural fault testability. After proving the baseline architecture achieves 100% fault coverage, intentional hardware redundancy (based on the Consensus Theorem) was injected to physically demonstrate **logic masking** and untestable faults.

**Team Members:** Mukund Rathi [2023BEC0051] & Aniketh Yuvaraj C. [2023BEC0049]  
**Course:** ECS324 VLSI Testing & Verification

## 🛠️ Toolchain & Methodology
* **Icarus Verilog & GTKWave:** RTL behavioral design and functional simulation.
* **Yosys:** Logic synthesis to gate-level netlist and Formal Equivalence Checking (EQY).
* **Vivado:** RTL Schematic generation.
* **Atalanta:** ATPG test pattern generation and fault simulation (FAN Algorithm).
* **Python:** Custom automation to map XOR logic into ISCAS89 `.bench` pure NAND formats to bypass legacy parser limitations.

## 📂 Repository Structure
**RTL & Synthesis:**
* `crc8.v` - Behavioral RTL Verilog code for the parallel CRC-8.
* `tb.v` - Testbench for verifying combinational functionality.
* `synth.ys` - Yosys synthesis script.
* `crc8_netlist.v` - Synthesized gate-level netlist.
* `equiv.ys` - Yosys script for formal equivalence checking.

**ATPG & Fault Analysis:**
* `gen_bench.py` & `gen.py` - Python scripts to generate NAND-based ISCAS89 bench files.
* `c8bitnormal.bench` - ISCAS89 benchmark file for the baseline CRC-8.
* `c8bitnormal.test` & `c8bitnormal.vec` - ATPG test vectors for the baseline architecture (100% Coverage).
* `c8bit.bench` - ISCAS89 benchmark file with injected Consensus Theorem redundancy.
* `c8bittest.test` & `c8bit.vec` - ATPG test vectors for the redundant architecture.
* `c8bit.ufaults` - List of identified redundant (untestable) faults.

**Documentation:**
* `Report_CRC8.pdf` - Full theoretical analysis, including manual D-Algorithm hand-tracing proofs.

## 📊 Key Findings
* **Baseline Architecture:** Achieved **100.000% fault coverage** with exactly 16 compact test patterns and 0 redundant faults due to the lack of reconvergent fanouts.
* **Modified Architecture (Redundancy Injected):** By injecting a $BC$ consensus term ($F = AB + A'C + BC$) as a static hazard cover, fault coverage correctly dropped to **97.934%**. The ATPG tool successfully isolated 5 redundant faults.
* **Manual Verification:** A manual D-Algorithm hand-trace was conducted to mathematically prove that excitation and propagation conditions for the $BC$ path fundamentally conflict, completely masking the fault and confirming the tool's output.
