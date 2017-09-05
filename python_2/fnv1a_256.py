#
# fnv-1a_256.py
#
# Fowler-Noll-Vo 1a 256 bits
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
# FNV offset basis
#
# 0xdd268dbcaac550362d98c384c4e576ccc8b1536847b6bbb31023b4c8caee0535
#

FNV1A_256_OFFSET = 0xdd268dbcaac550362d98c384c4e576ccc8b1536847b6bbb31023b4c8caee0535

#
# FNV prime
#
# 2^168 + 2^8 + 0x63
# 0x1000000000000000000000000000000000000000163
#

FNV1A_256_PRIME = 0x1000000000000000000000000000000000000000163





#
# FNV-1a 256 hash on a string
#

def fnv1a_256_str(string):
	
	# Set the offset basis
    hash = FNV1A_256_OFFSET

	# For each character
    for character in string:

		# Xor with the current character
        hash ^= ord(character)

		# Multiply by prime
        hash *= FNV1A_256_PRIME

		# Clamp
        hash &= 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

	# Return the final hash as a number
    return hash
