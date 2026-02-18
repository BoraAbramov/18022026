# 1
smokers = {"John Smith", "Maya Levi", "Noam Cohen", "Liam Patel"}
ride_bikes = {"Maya Levi", "Omer Halevi", "Liam Patel"}
ride_motorcycles = {"John Smith", "Noam Cohen", "Rina Gold"}
likes_skyjump = {"John Smith", "Rina Gold", "Dina Bar"}

print("Suspects:", {"John Smith","Maya Levi","Noam Cohen","Liam Patel","Omer Halevi","Rina Gold","Dina Bar"})
print("\nClues:")
print("1) The suspect SMOKES")
print("2) The suspect likes SKYDIVING")
print("3) The suspect rides a BIKE or a MOTORCYCLE")

print(f"The final suspect is {smokers & likes_skyjump & (ride_bikes | ride_motorcycles)}")
print("-" * 100)
# 2


smokers = {"Avi Ron", "Sara Kim", "Ben Azulay", "Nina Fox"}
ride_bikes = {"Sara Kim", "Tom Green", "Nina Fox"}
ride_motorcycles = {"Avi Ron", "Ben Azulay", "Nina Fox", "Eli Stone"}
likes_skyjump = {"Avi Ron", "Nina Fox", "Sara Kim", "Dana Wolf"}

print("Suspects:", {"Avi Ron","Sara Kim","Ben Azulay","Nina Fox","Tom Green","Eli Stone","Dana Wolf"})
print("\nClues:")
print("1) The suspect rides a BIKE or a MOTORCYCLE")
print("2) The suspect SMOKES")
print("3) The suspect likes SKYDIVING")
print("4) The suspect is NOT someone who rides BOTH bike AND motorcycle")

print(f"The final suspect {(ride_bikes | ride_motorcycles) & smokers & likes_skyjump - (ride_bikes & ride_motorcycles)}")