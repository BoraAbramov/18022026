
# Actors in Marvel Cinematic Universe (Main Avengers)
actors_mcu = {
    "Robert Downey Jr.",
    "Chris Evans",
    "Chris Hemsworth",
    "Mark Ruffalo",
    "Scarlett Johansson",
    "Jeremy Renner",
    "Tom Hiddleston",
    "Benedict Cumberbatch",
    "Paul Rudd",
    "Brie Larson",
    "Chadwick Boseman"
}

# Actors in DC Extended Universe
actors_dceu = {
    "Henry Cavill",
    "Ben Affleck",
    "Gal Gadot",
    "Jason Momoa",
    "Ezra Miller",
    "Ray Fisher",
    "Margot Robbie",
    "Will Smith",
    "Jared Leto",
    "Zachary Levi"
}

# Actors who have done superhero movies in general (including non-MCU/DCEU)
actors_superhero = {
    "Robert Downey Jr.",
    "Chris Evans",
    "Christian Bale",  # Batman (Dark Knight Trilogy)
    "Tobey Maguire",  # Spider-Man
    "Andrew Garfield",  # Spider-Man
    "Hugh Jackman",  # X-Men
    "Patrick Stewart",  # X-Men
    "Ian McKellen",  # X-Men
    "Ryan Reynolds",  # Deadpool
    "Michael Keaton",  # Batman
    "Ben Affleck",
    "Gal Gadot"
}

print(f"\n🦸 Actors in Marvel Cinematic Universe: {actors_mcu}")

print(f"\n🦇 Actors in DC Extended Universe: {actors_dceu}")

print(f"\n🎭 Actors in superhero movies (any franchise): {actors_superhero | actors_dceu | actors_mcu}")

_both = actors_mcu & actors_dceu
print(f"\n❓ Are there any actors in BOTH MCU and DCEU? {_both}")

s1 = actors_superhero - actors_mcu
print(f"\n❓ Actors in superhero movies but NOT in MCU? {s1}")

s2 = actors_dceu <= actors_superhero
print(f"\n❓ Is the DCEU set a subset of any superhero actors? {s2}")

s3 = actors_mcu - actors_superhero - actors_dceu
print(f"\n❓ Actors ONLY in MCU (not in other franchises)? {s3}")

s4 = actors_superhero >= actors_mcu
print(f"\n❓ Is all_superhero_actors a superset of DCEU? {s4}")
