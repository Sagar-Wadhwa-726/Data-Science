# Set storing the hike of the employees
hikes = {
    "Dhwani":100,
    "Sagar":100,
    "Aryan":10,
    "Shivi":10
}

print(hikes.keys())
print(hikes.values())
print(hikes["Dhwani"])
print(hikes["Shivi"])
hikes["Shivi"]=0
print(hikes["Shivi"])

x = hikes.items() # stores the items of the dictionary in the list
y =hikes.popitem() # pops the last item of the dictionary
z=hikes.get("Aryan")
print(x, y,z)
hikes.pop("Aryan")
hikes.update(Dhwani=106, Sagar=106)
print(hikes)
