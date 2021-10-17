# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Parmjeet Jailwal"

first_name = name[:8]       #  [0:8]
last_name = name[9:]        #  [9:end]
funky_name = name[::2]      #  [0:end:2]
reversed_name = name[::-1]  #  [0:end:-1]

print(first_name)
print(last_name)
print(funky_name)
print(reversed_name)

website1 = "https://google.com"
website2 = "https://wikipedia.com"

slice = slice(8,-4)

print(website1[slice])
print(website2[slice])