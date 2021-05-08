def ip_address(address):
    new_address = ""
    split_address = address.split(".")
    separator = "[.]"
    new_address = separator.join(split_address)

    return new_address


ip_address("1.1.1.1")
print(ip_address)
print(id(ip_address))
print(ip_address("1.1.1.1"))


# def ip_address2(address):
#     new_address = ""
#     split_address = address.split("[.]")
#     separator = "."
#     new_address = separator.join(split_address)
#     return new_address


# print(ip_address2("1[.]2[.]3[.]4"))
# print(id(ip_address2))
