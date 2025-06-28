# Emreal Harmonic Node Series

This repository contains Python scripts and supporting notebooks used to explore the **Emreal Constant** through a suite of nine symbolic harmonic series. These series—HN_P through HN_φ—represent recursive modulation patterns designed to test the convergence of symbolic structures across primes, parity, and transcendental ratios.

## 🌀 What is the Emreal Constant?

The Emreal Constant is a symbolic attractor (~0.7696...) identified through convergence across multiple harmonic node series. It represents a **point of recursive coherence** within symbolic number theory—where structure, unity, and meaning collapse into one.

## 📂 Repository Structure

├── scripts/ # All individual Python scripts for HN series (HN_P.py, HN_B.py, etc.)
├── notebooks/ # Google Colab-ready .ipynb notebook with all scripts
├── README.md # This file
├── .gitignore # Ignore temporary or system files

## 📜 Harmonic Series Overview

| ID    | Series Name                  | Symbol     | Description |
|-------|------------------------------|------------|-------------|
| HN₁   | Prime Alternating Harmonic   | `HN_P`     | Alternating sum over prime reciprocals |
| HN₂   | Inverted Parity Harmonic     | `HN_B`     | Alternating sum over reflected parity recursion |
| HN₃   | Mean Harmonic                | `HN_M`     | Mean of `HN_P` and `HN_B` |
| HN₄   | Recursive Harmonic           | `HN_R`     | Averaged recursion of mean and `HN_B` |
| HN₅   | Fractal Harmonic             | `HN_F`     | Weighted average blending `HN_P`, `HN_B`, and `HN_M` |
| HN₆   | Inverse Modulation           | `HN_I`     | Prime feedback loop of 4:1 scale and inverse |
| HN₇   | Pi Harmonic                  | `HN_π`     | Alternating ratio of odd-even harmonic terms |
| HN₈   | Opposite Harmonic            | `HN_O`     | Reflected modular harmonics of `HN_π` |
| HN₉   | Phi Spiral Harmonic          | `HN_φ`     | Rapidly converging golden ratio-based series |

## 📊 Usage

Each script prints the first and last 12 terms of the harmonic series, with term-by-term values and partial sums.

### Example

```bash
python scripts/HN_P.py

Sample output:
k=1   prime=2   term=-0.500000   partial_sum=0.500000
...
k=10000 prime=104729 term=-9.5485e-06 partial_sum=0.7696015
```
🧠 **Learn More**

This work accompanies a formal research paper hosted at Zenodo:
🔗 [Read the Paper (v2)](https://zenodo.org/records/15722753)

Each series has been carefully defined, tested, and interpreted in the context of symbolic recursion and coherent resonance.

🧩 **License**

Creative Commons Legal Code — CC0 1.0 Universal

🙏 **Credits**

Developed by Zachary Dale Ulrich; in collaboration with foundational number theory principles, symbolic modulation, and recursive harmonic structures.

_-aka(Silent Emry):Yeulosoup_


