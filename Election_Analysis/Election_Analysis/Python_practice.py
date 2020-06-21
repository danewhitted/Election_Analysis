print("Hello World")
n=2
print (n)
counties_dict = {}
counties_dict["Arapahoe"] = 422829
print (counties_dict)

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

temperature = int(input("What is the temperature outside? "))

if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")