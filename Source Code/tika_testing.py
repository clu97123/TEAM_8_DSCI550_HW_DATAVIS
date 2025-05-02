from tika import parser
parsed = parser.from_file("alice_texas_8760.png")
print(parsed["metadata"])
