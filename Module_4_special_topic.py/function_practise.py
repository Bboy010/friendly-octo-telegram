def gc_content(sequence, uppercase=True, detailed=False):
    if not uppercase:
        sequence = sequence.upper()

    g_count = sequence.count('G')
    c_count = sequence.count('C')
    a_count = sequence.count('A')
    t_count = sequence.count('T')

    gc_content_percentage = ((g_count + c_count) / len(sequence)) * 100

    if detailed:
        print(f"G count: {g_count}")
        print(f"C count: {c_count}")
        print(f"A count: {a_count}")
        print(f"T count: {t_count}")

    return gc_content_percentage

# Example usage
print(gc_content("atgcgtac", uppercase=False, detailed=True))
print(gc_content("ATGCGTAC", detailed=True))
#16 returning mul value