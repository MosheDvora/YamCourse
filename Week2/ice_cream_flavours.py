ice_cream_flavours = ['chocolate', 'vanilla', 'pistachio', 'banana']

user_favorit = input("What is your favorit ice cream flavour? \n")
print("We have your favorit flavour " if user_favorit in ice_cream_flavours else "Sorry we don't have this flavor")