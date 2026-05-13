justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print(f"1. Total members: {len(justice_league)}")

justice_league.extend(["Batgirl", "Nightwing"])
print(f"2. New team after recruitement{justice_league}")

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(f"3. Moving new leader at front: {justice_league}")

justice_league.remove("Superman")
aquaman_idx = justice_league.index("Aquaman")
justice_league.insert(aquaman_idx, "Superman")
print(f"4. Seperate Flash and Aquaman: {justice_league}")

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print(f"5. Crisis Team: {justice_league}")

justice_league.sort()
new_leader = justice_league[0]
print(f"6. Sorted list: {justice_league}")
print(f"The new leader is: {new_leader}")