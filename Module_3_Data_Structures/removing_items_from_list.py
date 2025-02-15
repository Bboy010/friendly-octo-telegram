species = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla", "Felis catus", "Canis lupus"]

# Remove a specific species

species.remove("Felis catus")

print(f"{species} \n")

# Remove the last species

species.pop()

print(f"{species} \n")

# Remove a species by index

del species[1]

print(species)