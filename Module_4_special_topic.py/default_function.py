def gc_content(sequence, uppercase=True):

    if not uppercase:

        sequence = sequence.upper()

    g_count = sequence.count('G')

    c_count = sequence.count('C')

    gc_content_percentage = ((g_count + c_count) / len(sequence)) * 100

    return gc_content_percentage

print(gc_content("atgcgtac", uppercase=False))

print(gc_content("ATGCGTAC"))