#this function return multiple value
def gc_at_content(sequence):
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    a_count = sequence.count('A')
    t_count = sequence.count('T')
    gc_content_percentage = ((g_count + c_count) / len(sequence)) * 100
    at_content_percentage = ((a_count + t_count) / len(sequence)) * 100
    return gc_content_percentage, at_content_percentage

gc, at = gc_at_content("ATGCGTAC")
print(f"GC content: {gc:.2f}%")
print(f"AT content: {at:.2f}%")