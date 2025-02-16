dna_sequences = ["ATGCGTAC", "GCTTAGCT", "CGTACGTA"]



for seq in dna_sequences:

    g_count = seq.count('G')

    c_count = seq.count('C')

    gc_content = ((g_count + c_count) / len(seq)) * 100

    print(f"GC content of {seq}: {gc_content:.2f}%")

