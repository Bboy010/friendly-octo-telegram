# # Team Instructions:

# ## As usual, you can decide to use Python or R, even within a team, but:
# You have to provide all 4 functions for each language when submitting
# ---
# # Tasks : Functions Galore!
# 1. Write a function for translating DNA to protein
# 2. Write a function that simulates and generates a logistic population growth curve. 
# * Your function should include 2 extra parameters that randomize the length of the lag phase and the exponential phase [See population curve here]. 
# * Most living populations follow a logistic population growth.
# * Therefore, your growth curve can be: 
#     * Population Size vs Time, 
#     * Cell density vs Time, 
#     * OD vs Time, 
#     * CFU vs Time, etc
# 3. Using your function, generate a dataframe with 100 different growth curves
# 4. Write a function for determining the time to reach 80% of the maximum growth; usually the carrying capacity
# 5. Finally, write a function for calculating the hamming distance between your Slack username and twitter/X handle (synthesize if you don’t have one). Feel free to pad it with extra words if they are not of the same length.

"""define the functions dna_to_protein
    This function takes a DNA sequence as input and returns the corresponding protein sequence"""
def dna_to_protein(dna):
    genetic_code = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein = ""
    if len(dna)%3 == 0:
        for i in range(0, len(dna), 3):
            codon = dna[i:i + 3]
            protein+= genetic_code[codon]
    return protein

"""define the functions logistic_population_growth
    This function takes the lag phase and exponential phase as input and returns the population growth curve"""
def logistic_population_growth(lag_phase, exp_phase):
    time = np.linspace(0, 100, 100)
    population = []
    for t in time:
        population.append(1/(1 + np.exp(-0.1*(t - lag_phase))))
    return pd.DataFrame({'Time': time
                         , 'Population': population})

"""define the functions time_to_80_percent_growth
    This function takes the lag phase and exponential phase as input and returns the time to reach 80% of the maximum growth"""
def time_to_80_percent_growth(lag_phase, exp_phase):
    import numpy as np
    time = np.linspace(0, 100, 100)
    population = []
    for t in time:
        population.append(1/(1 + np.exp(-0.1*(t - lag_phase))))
    return time[population.index(max(population))]*0.8

"""define hamming_distance
this function calculate the harmming distance between two strings"""
def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        return "Strings are not of the same length"
    else:
        return sum([1 for i in range(len(s1)) if s1[i] != s2[i]])
    
#  Example usage of dna_to_protein
print(dna_to_protein("CCTCCCACCCGTGTTTACTGTACCTTAGTTGCTTCGGCGGGCCCGCCGCAAGGCCGCCGGGGGGCATCCGCCCCCGGGCCCGCGCCCGCCGGAGACACCACGAACTCTGAACGATCTAGTGAAGTCTGAGTTGATTGTATCGCAATCAGTTAAAACTTTCAACAATGGATCTCTTGGTTCCGGCATCGATGAAGAACGCAGCGAAATGCGATAACTAGTGTGAATTGCAGAATTCCGTGAATCATCGAGTCTTTGAACGCACATTGCGCCCCCTGGTATTCCGGGGGGCATGCCTGTCCGAGCGTCATTGCTGCCCATCAAGCACGGCTTGTGTGTTGGGTCGTCGTCCCCCTCTCCGGGGGGGGACGGGCCCTAAAGGCAGCGGCGGCACCGCGTCCGATCCTCGAGCGTATGGGGCTTTGTCACCCGCTCTGTAGGCCCGGCCGGCGCTTGCCGAACGCAAAACAACCA"))
# Trichoderma sp. isolate Plastic dumped Soil internal transcribed spacer 1, partial sequence; 5.8S ribosomal RNA gene, complete sequence; and internal transcribed spacer 2, partial sequence

#testing Using your function, generate a dataframe with 100 different growth curves with function 2
growth_curve = 100*[logistic_population_growth(random.randint(0, 100), random.randint(0, 100))]
print(growth_curve)


# # Example usage of time_to_80_percent_growth
lag_phase = 20  # Example lag phase
exp_phase = 50  # Example exponential phase

time_80 = time_to_80_percent_growth(lag_phase, exp_phase)
print(f"Time to reach 80% of maximum population: {time_80}")

# # Example usage of hamming_distance
string1 = "ATGC"
string2 = "ATGC"
distance = hamming_distance(string1, string2)
print(f"Hamming distance between '{string1}' and '{string2}': {distance}")

string3 = "GAGCCTACTAACGGGAT"
string4 = "CATCGTAATGACGGCCT"
distance = hamming_distance(string3, string4)
print(f"Hamming distance between '{string3}' and '{string4}': {distance}")

## HOngo