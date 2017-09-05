#
# test_vectors.py
#
# Fowler-Noll-Vo 1a
#
# Copyright 2017 Philippe Paquet
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#





#
# imports
#

from fnv1a_32 import fnv1a_32_str 
from fnv1a_64 import fnv1a_64_str
from fnv1a_128 import fnv1a_128_str
from fnv1a_256 import fnv1a_256_str
from fnv1a_512 import fnv1a_512_str
from fnv1a_1024 import fnv1a_1024_str





#
# 32 bits test vectors
#

fnv1a_32_vectors = {	"":				0x811c9dc5,
						"a":			0xe40c292c,
						"b":			0xe70c2de5,
						"c":			0xe60c2c52,
						"d":			0xe10c2473,
						"e":			0xe00c22e0,
						"f":			0xe30c2799,
						"fo":			0x6222e842,
						"foo":			0xa9f37ed7,
						"foob":			0x3f5076ef,
						"fooba":		0x39aaa18a,
						"foobar":		0xbf9cf968}

#
# 64 bits test vectors
#

fnv1a_64_vectors = {	"":				0xcbf29ce484222325,
						"a":			0xaf63dc4c8601ec8c,
						"b":			0xaf63df4c8601f1a5,
						"c":			0xaf63de4c8601eff2,
						"d":			0xaf63d94c8601e773,
						"e":			0xaf63d84c8601e5c0,
						"f":			0xaf63db4c8601ead9,
						"fo":			0x08985907b541d342,
						"foo":			0xdcb27518fed9d577,
						"foob":			0xdd120e790c2512af,
						"fooba":		0xcac165afa2fef40a,
						"foobar":		0x85944171f73967e8}

#
# 128 bits test vectors
#

fnv1a_128_vectors = {	"":				0x6c62272e07bb014262b821756295c58d,
						"a":			0xd228cb696f1a8caf78912b704e4a8964,
						"b":			0xd228cb69721a8caf78912b704e4a8d15,
						"c":			0xd228cb69711a8caf78912b704e4a8bda,
						"d":			0xd228cb696c1a8caf78912b704e4a85b3,
						"e":			0xd228cb696b1a8caf78912b704e4a8478,
						"f":			0xd228cb696e1a8caf78912b704e4a8829,
						"fo":			0x08809542c0ab1be95aa0733055b5ae22,
						"foo":			0xa68d5ed15f8b5822836dbc79768d78bf,
						"foob":			0x696a39196d757277b806e974e013b7ef,
						"fooba":		0x2a9456013d83d94f708142cfb842dbba,
						"foobar":		0x343e1662793c64bf6f0d3597ba446f18}

#
# 256 bits test vectors
#

fnv1a_256_vectors = {	"":				0xdd268dbcaac550362d98c384c4e576ccc8b1536847b6bbb31023b4c8caee0535,
						"a":			0x63323fb0f35303ec28dc751d0a33bdfa4de6a99b7266494f6183b2716811637c,
						"b":			0x63323fb0f35303ec28dc781d0a33bdfa4de6a99b7266494f6183b271681167a5,
						"c":			0x63323fb0f35303ec28dc771d0a33bdfa4de6a99b7266494f6183b27168116642,
						"d":			0x63323fb0f35303ec28dc721d0a33bdfa4de6a99b7266494f6183b27168115f53,
						"e":			0x63323fb0f35303ec28dc711d0a33bdfa4de6a99b7266494f6183b27168115df0,
						"f":			0x63323fb0f35303ec28dc741d0a33bdfa4de6a99b7266494f6183b27168116219,
						"fo":			0xf4f7a1c2efd0e1e4bb177a4525c0721a06dd328fa3d7a91439a07343501b89a2,
						"foo":			0x8b0e658c2f1c837f8d185ae359de3a1784bd1d30340f770be97fd65816301747,
						"foob":			0xe46ddd4ed460b1f6d8dd2e459f2a8e9d123f79d831721584cc463c26c4b0184f,
						"fooba":		0x366f691cc852f0136acf588bb803c3d04e05f6cc9133d727456569c2c03187ca,
						"foobar":		0xb055ea2f306cadad4f0f81c02d3889dc32453dad5ae35b753ba1a91084af3428}

#
# 512 bits test vectors
#

fnv1a_512_vectors = {	"":				0xb86db0b1171f4416dca1e50f309990acac87d059c90000000000000000000d21e948f68a34c192f62ea79bc942dbe7ce182036415f56e34bac982aac4afe9fd9,
						"a":			0xe43a992dc8fc5ad7de493e3d696d6f85d64326ec07000000000000000011986f90c2532caf5be7d88291baa894a395225328b196bd6a8a643fe12cd87b27ff88,
						"b":			0xe43a992dc8fc5ad7de493e3d696d6f85d64326ec0a000000000000000011986f90c2532caf5be7d88291baa894a395225328b196bd6a8a643fe12cd87b28038d,
						"c":			0xe43a992dc8fc5ad7de493e3d696d6f85d64326ec09000000000000000011986f90c2532caf5be7d88291baa894a395225328b196bd6a8a643fe12cd87b280236,
						"d":			0xe43a992dc8fc5ad7de493e3d696d6f85d64326ec0c000000000000000011986f90c2532caf5be7d88291baa894a395225328b196bd6a8a643fe12cd87b28063b,
						"e":			0xe43a992dc8fc5ad7de493e3d696d6f85d64326ec0b000000000000000011986f90c2532caf5be7d88291baa894a395225328b196bd6a8a643fe12cd87b2804e4,
						"f":			0xe43a992dc8fc5ad7de493e3d696d6f85d64326ec0e000000000000000011986f90c2532caf5be7d88291baa894a395225328b196bd6a8a643fe12cd87b2808e9,
						"fo":			0x7317dfed6c70dfec6adfced2a5e04d7eec744e4f480000000000000017933d7af45d70def423a316f14117df272cd0fd6b85f0f7c9bf6c5196b3160d02a36b8a,
						"foo":			0x142433ed48a78bb429a7dba8911e8824dcd78fa55d0000000000001f96475fbd69323ab91bbf83bd3e36fbfd7d0c038b1075dbff4f7a2150e9f28b6e88f58fd3,
						"foob":			0xf9fe9eefe38ca43fcf36c8fbc0d25bef535a6c1f4c00000000002a5259a146c7f24cae042d99828e5baba0a28b18bf530de9c3137ca2a36973f8d11981038627,
						"fooba":		0x96b20c29347dfb41b5e3ebf2c34d2679c7a7e1751a0000000038b4561715d5e5a4bd279918adecbcd2f439c85e285847a4345f1bfde8f24a6260292bdbb8e7ca,
						"foobar":		0xb0ec738d9c6fd969d05f0b35f6c0ed53adcacccd8e0000004bf99f58ee4196afb9700e20110830fea5396b76280e47fd022b6e81331ca1a9ced729c364be7788}

#
# 1024 bits test vectors
#

fnv1a_1024_vectors = {	"":				0x0000000000000000005f7a76758ecc4d32e56d5a591028b74b29fc4223fdada16c3bf34eda3674da9a21d9000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004c6d7eb6e73802734510a555f256cc005ae556bde8cc9c6a93b21aff4b16c71ee90b3,
						"a":			0x000000000000000098d7c19fbce653df221b9f717d3490ff95ca87fdaef30d1b823372f85b24a372f50e570000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007685cd81a491dbccc21ad06648d09a5c8cf5a78482054e91470b33dde77252caef695aa,
						"b":			0x000000000000000098d7c19fbce653df221b9f717d3490ff95ca87fdaef30d1b823372f85b24a372f50e560000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007685cd81a491dbccc21ad06648d09a5c8cf5a78482054e91470b33dde77252caef6941d,
						"c":			0x000000000000000098d7c19fbce653df221b9f717d3490ff95ca87fdaef30d1b823372f85b24a372f50e550000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007685cd81a491dbccc21ad06648d09a5c8cf5a78482054e91470b33dde77252caef69290,
						"d":			0x000000000000000098d7c19fbce653df221b9f717d3490ff95ca87fdaef30d1b823372f85b24a372f50e5c0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007685cd81a491dbccc21ad06648d09a5c8cf5a78482054e91470b33dde77252caef69d6b,
						"e":			0x000000000000000098d7c19fbce653df221b9f717d3490ff95ca87fdaef30d1b823372f85b24a372f50e5b0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007685cd81a491dbccc21ad06648d09a5c8cf5a78482054e91470b33dde77252caef69bde,
						"f":			0x000000000000000098d7c19fbce653df221b9f717d3490ff95ca87fdaef30d1b823372f85b24a372f50e5a0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000007685cd81a491dbccc21ad06648d09a5c8cf5a78482054e91470b33dde77252caef69a51,
						"fo":			0x00000000000000f46ef41cd23a4dcdd406834963b78e82241a6f5cb06f403cbd5a7c8903cef6a5f4fddbd00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000b7cd7fb20c3631dc8903952e9eeb7f618698f4c87da23ad74b2c5f6f1fec4a64b546d3226,
						"foo":			0x000000000001868ce88bd2c7cdc5fa5e52ebb9925ff5ea668dff4576aa4ba65819176ce6b925a8421b13d9000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000011d09af071cf00b53007a8e594c73348a3dbb339aead4953fdf93cfff54816f5e2d1ed56fb35,
						"foob":			0x00000000026f791f9147aedad1354bef7d238f3219005cbd6e8d664f6b4eefdbe94929e41548c07154c2dc000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001ba08046e07e0418fb7be0ec07b8ea87a61bb4f073e2bab740db8398ef60cb9b50bf8d0fe3c5eb,
						"fooba":		0x00000003e27f563b2ca82d6f6b22a35117ddfb386bab86b4e52a63e0aa457ba1b5d6c2505291fcd055f4b60000000000000000000000000000000000000000000000000000000000000000000000000000000000000000002ad7e6edea236c5abdff1bce07f9c3b45c98f798e3b69b8e2f946b142b391bbfdc390dc1a4395702,
						"foobar":		0x00000631175fa7ae643ad08723d312c9fd024adb91f77f6b19587197a22bcdf23727166c4572d0b985d5ae00000000000000000000000000000000000000000000000000000000000000000000000000000000000000004270d11ef418ef08b8a49e1e825e547eb39937f819222f3b7fc92a0e4707900888847a554bacec98b0}





#
# Test vectors for 32 bits
#

def test_vectors_32():

	global fnv1a_32_vectors

	# The test pass unless we have at least one fail
	failed = False;

	# Go through test vectors
	for string, result in fnv1a_32_vectors.items():
		if (fnv1a_32_str(string) != result):
			print("fnv1a_32_str test failed for \"" + string + "\"")
			print(hex(fnv1a_32_str(string)) + " returned")
			print(hex(result) + " expected")
			failed = True

	# Check results
	if (False == failed):
		print("fnv1a_32_str successfully tested")



#
# Test vectors for 64 bits
#

def test_vectors_64():

	global fnv1a_64_vectors

	# The test pass unless we have at least one fail
	failed = False;

	# Go through test vectors
	for string, result in fnv1a_64_vectors.items():
		if (fnv1a_64_str(string) != result):
			print("fnv1a_64_str test failed for \"" + string + "\"")
			print(hex(fnv1a_64_str(string)) + " returned")
			print(hex(result) + " expected")
			failed = True

	# Check results
	if (False == failed):
		print("fnv1a_64_str successfully tested")



#
# Test vectors for 128 bits
#

def test_vectors_128():

	global fnv1a_128_vectors

	# The test pass unless we have at least one fail
	failed = False;

	# Go through test vectors
	for string, result in fnv1a_128_vectors.items():
		if (fnv1a_128_str(string) != result):
			print("fnv1a_128_str test failed for \"" + string + "\"")
			print(hex(fnv1a_128_str(string)) + " returned")
			print(hex(result) + " expected")
			failed = True

	# Check results
	if (False == failed):
		print("fnv1a_128_str successfully tested")



#
# Test vectors for 256 bits
#

def test_vectors_256():

	global fnv1a_256_vectors

	# The test pass unless we have at least one fail
	failed = False;

	# Go through test vectors
	for string, result in fnv1a_256_vectors.items():
		if (fnv1a_256_str(string) != result):
			print("fnv1a_256_str test failed for \"" + string + "\"")
			print(hex(fnv1a_256_str(string)) + " returned")
			print(hex(result) + " expected")
			failed = True

	# Check results
	if (False == failed):
		print("fnv1a_256_str successfully tested")



#
# Test vectors for 512 bits
#

def test_vectors_512():

	global fnv1a_512_vectors

	# The test pass unless we have at least one fail
	failed = False;

	# Go through test vectors
	for string, result in fnv1a_512_vectors.items():
		if (fnv1a_512_str(string) != result):
			print("fnv1a_512_str test failed for \"" + string + "\"")
			print(hex(fnv1a_512_str(string)) + " returned")
			print(hex(result) + " expected")
			failed = True

	# Check results
	if (False == failed):
		print("fnv1a_512_str successfully tested")



#
# Test vectors for 1024 bits
#

def test_vectors_1024():

	global fnv1a_1024_vectors

	# The test pass unless we have at least one fail
	failed = False;

	# Go through test vectors
	for string, result in fnv1a_1024_vectors.items():
		if (fnv1a_1024_str(string) != result):
			print("fnv1a_1024_str test failed for \"" + string + "\"")
			print(hex(fnv1a_1024_str(string)) + " returned")
			print(hex(result) + " expected")
			failed = True

	# Check results
	if (False == failed):
		print("fnv1a_1024_str successfully tested")





test_vectors_32()
test_vectors_64()
test_vectors_128()
test_vectors_256()
test_vectors_512()
test_vectors_1024()
