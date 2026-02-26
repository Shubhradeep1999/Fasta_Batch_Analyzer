import csv
import matplotlib.pyplot as plt
import os
#FASTA FILE INPUT
fasta_file = input("Enter the path to the FASTA file: ")
try:
    file = open(fasta_file, 'r')
except:
    print("Error: File not found. Please check the path and try again.")
    exit()
#Detecting new sequences and merging lines
sequences = {}
seq_id = ""
seq = ""

with open(fasta_file, 'r') as file:
    for line in file:
        line = line.strip()
        if line.startswith(">"):
            if seq != "":
                sequences[seq_id] = seq
                seq = ""
            seq_id = line[1:]  # Remove '>' from the header
        else:
            seq += line
    if seq_id != "":
        sequences[seq_id] = seq  # Add the last sequence
#Analyzing each sequence
results = []
gc_values = []
length_values = []

total_A = 0
total_T = 0
total_G = 0
total_C = 0

for key in sequences:
    sequence = sequences[key].upper()

    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

    total_A += a
    total_T += t
    total_G += g
    total_C += c

    length = len(sequence)
    if length == 0:
        continue  # Skip empty sequences

    gc = ((g + c) / length) * 100

    gc = round(gc, 2)

    gc_values.append(gc)
    length_values.append(length)

    results.append([key, length, a, t, g, c, gc])

#Average GC content

if len(gc_values) > 0:
    average_gc = round(sum(gc_values) / len(gc_values), 2)
else:
    average_gc = 0

#Saving results to CSV

with open("../results/report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Sequence ID", "Length", "A", "T", "G", "C", "GC Content"])
    for row in results:
        writer.writerow(row)
    writer.writerow([])
    writer.writerow(["Average GC Content (%)", average_gc])

#Plotting GC content distribution
plt.figure(figsize=(10, 6))
plt.hist(gc_values)
plt.xlabel("GC Content (%)")
plt.ylabel("Frequency")
plt.title("GC Content Distribution")
plt.grid(True)
plt.tight_layout()
plt.savefig("../results/gc_content_distribution.png", dpi=300)
plt.close()

#Plotting sequence length distribution
plt.figure(figsize=(10, 6))
plt.hist(length_values)
plt.xlabel("Sequence Length")
plt.ylabel("Frequency")
plt.title("Sequence Length Distribution")
plt.grid(True)
plt.tight_layout()
plt.savefig("../results/sequence_length_distribution.png", dpi=300)
plt.close()

#Plotting Nucleotide composition
plt.figure(figsize=(8,8))
labels = ["A", "T", "G", "C"]
values = [total_A, total_T, total_G, total_C]

plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Nucleotide Composition")
plt.savefig("../results/nucleotide_composition.png", dpi=300)
plt.close()

#Final Output

print("\nBatch Fasta Analysis Completed!")
print("Sequence-wise GC values stored.")
print("Average GC Content:", average_gc)
print("CSV + Plots saved in results folder.\n")