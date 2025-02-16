sequences = ["ATG", "TGC", "CGA"]



for seq1 in sequences:

    for seq2 in sequences:

        if seq1 != seq2:

            print(f"Comparing {seq1} with {seq2}")
            print(f"Number of differences: {sum([1 for s1, s2 in zip(seq1, seq2) if s1 != s2])}")
            # Modify the nested loop to print the Hamming distance (number of differing positions) between each pair of sequences.
            # The Hamming distance is the number of positions at which the corresponding nucleotides are different.
            # For example, the Hamming distance between "ATG" and "TGC" is 3.
            # The Hamming distance between "ATG" and "CGA" is 3.
