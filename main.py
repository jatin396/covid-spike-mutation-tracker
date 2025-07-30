from Bio import SeqIO 


record1 = SeqIO.read("covid_sample1.fasta", "fasta")
print("Sample 1 ID:", record1.id)
print("Sample 1 sequence:")
print(record1.seq)


record2 = SeqIO.read("covid_sample2.fasta", "fasta")
print("\nSample 2 ID:", record2.id)
print("Sample 2 sequence:")
print(record2.seq)


seq1 = record1.seq
seq2 = record2.seq


if len(seq1) != len(seq2):
    print("\n Sequences are not the same length. Cannot compare.")
else:
    print("\n Mutations found:")
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            print(f"Position {i+1}: {seq1[i]} ➡ {seq2[i]}")

# Simulated spike region (from position 30 to 90)
spike_seq1 = seq1[29:90]  
spike_seq2 = seq2[29:90]

print("\n Spike-like region from Sample 1:\n", spike_seq1)
print("\n Spike-like region from Sample 2:\n", spike_seq2)

print("\n Mutations in Spike-like region:")
for i in range(len(spike_seq1)):
    if spike_seq1[i] != spike_seq2[i]:
        print(f"Position {i+30}: {spike_seq1[i]} ➡ {spike_seq2[i]}")
