def at_content(sequence):

    a_count = sequence.count('A')

    t_count = sequence.count('T')

    at_content_percentage = ((a_count + t_count) / len(sequence)) * 100

    return at_content_percentage

dna_sequence = "ATGCGTAC"

at = at_content(dna_sequence)

print(f"AT content of {dna_sequence}: {at:.2f}%")