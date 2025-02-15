sequence = ["ATGCGTAC", "GCTTAGCT", "CGTACGTA"]

g = sequence[0].count('G')

c = sequence[0].count('C')

gc_content_percentage = ((g + c) / len(sequence[0])) * 100

print(g)
print(c)
print(len(sequence[0]) )
print(gc_content_percentage)
