# test_smqtk.py
from smqtk_descriptors.impls.descriptor_generator.random import RandomDescriptorGenerator

gen = RandomDescriptorGenerator()
vec = gen.generate_one('images/woodland_park_colorado_10991.png')
print(vec)
