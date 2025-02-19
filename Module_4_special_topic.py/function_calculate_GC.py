def gc_content(sequence):

    g_count = sequence.count('G')

    c_count = sequence.count('C')

    gc_content_percentage = ((g_count + c_count) / len(sequence)) * 100

    return gc_content_percentage

dna_sequence = "ATGCGTAC"

gc = gc_content(dna_sequence)

print(f"GC content of {dna_sequence}: {gc:.2f}%")
# print(f"GC content of {dna_sequence}: {gc:.2f}%")