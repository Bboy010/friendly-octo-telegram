species = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]



# Add a new species to the list

species.append("Macaca mulatta")

print(species)  # Output: ['Homo sapiens', 'Pan troglodytes', 'Pongo pygmaeus', 'Macaca mulatta']

print("="*20)

# Add multiple species at once

species.extend(["Felis catus", "Canis lupus"])

print(species)