# COVID Spike Mutation Tracker 🧬

In this project, I compare two COVID-19 genome sequences to detect mutations. My focus is on the **Spike protein region** (the part of the virus that helps it enter human cells). This may help bioinformaticians detect and track those changes.

## 💻 How It Works

1. Input: Two DNA samples in FASTA format
2. Reads sequences using **Biopython**
3. Compares them to:
   - Find full-genome mutations
   - Focus on Spike-like region (positions 30–90)
4. Prints exact mutation positions and changes

## 📁 Files used.

- `covid_sample1.fasta` – Reference genome
- `covid_sample2.fasta` – Mutated sample
- `main.py` – Core logic (sequence reading + mutation detection)
- `README.md` – Project summary

###Created by###
jatin

