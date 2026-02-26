Batch FASTA Analyzer with GC Content Report
# Project Overview

This project is a Python-based bioinformatics pipeline designed to perform batch analysis of biological sequences from FASTA files. The program processes multiple sequences automatically and generates statistical reports along with visualizations for exploratory sequence analysis.

# Objectives

Detect new sequences from FASTA headers

Merge multi-line biological sequences

Calculate nucleotide composition (A/T/G/C)

Compute GC content (%) for each sequence

Calculate average GC content across dataset

Store sequence-wise results programmatically

Export results into CSV format

Generate visual plots for:

GC Content Distribution

Sequence Length Distribution

Nucleotide Composition

#️ Tools Used

Python

Ubuntu (Linux Terminal)

Matplotlib

VS Code

# Output Generated

Sequence-wise GC Content Report (CSV)

Average GC Content Calculation

GC Content Histogram

Sequence Length Distribution Plot

Nucleotide Composition Pie Chart

# How to Run
python3 batch_analyzer.py

# Sample Output

All outputs are saved in:

results/

Including:

report.csv

gc_distribution.png

length_distribution.png

nucleotide_composition.png