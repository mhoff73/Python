grace_hopper = []
grace_hopper.extend(["Holia", "Fancesca"])
grace_hopper.extend(["Talya", "Ann", "Gloria"])
grace_hopper.remove("Ann")
grace_hopper.insert(2, "Dewan")
grace_hopper.pop(len(grace_hopper)-1)
for students in grace_hopper:
  print(students)
print(len(grace_hopper))
grace_hopper[3] = "Abigail"
