#
# fnv-1a_128.py
#
# Fowler-Noll-Vo 1a 128 bits
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
# 0x6c62272e07bb014262b821756295c58d
#

FNV1A_128_OFFSET = 0x6c62272e07bb014262b821756295c58d

#
# FNV prime
#
# 2^88 + 2^8 + 0x3b
# 0x1000000000000000000013b
#

FNV1A_128_PRIME = 0x1000000000000000000013b





#
# FNV-1a 128 hash on a string
#

def fnv1a_128_str(string):
	
	# Set the offset basis
	hash = FNV1A_128_OFFSET

	# For each character
	for character in string:

		# Xor with the current character
		hash ^= ord(character)

		# Multiply by prime
		hash *= FNV1A_128_PRIME

		# Clamp
		hash &= 0xffffffffffffffffffffffffffffffff

	# Return the final hash as a number
	return hash
