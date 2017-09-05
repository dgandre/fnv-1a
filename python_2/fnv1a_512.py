#
# fnv-1a_512.py
#
# Fowler-Noll-Vo 1a 512 bits
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
# 0xb86db0b1171f4416dca1e50f309990acac87d059c90000000000000000000d21e948f68a34c192f62ea79bc942dbe7ce182036415f56e34bac982aac4afe9fd9
#

FNV1A_512_OFFSET = 0xb86db0b1171f4416dca1e50f309990acac87d059c90000000000000000000d21e948f68a34c192f62ea79bc942dbe7ce182036415f56e34bac982aac4afe9fd9

#
# FNV prime
#
# 2^344 + 2^8 + 0x57
# 0x100000000000000000000000000000000000000000000000000000000000000000000000000000000000157
#

FNV1A_512_PRIME = 0x100000000000000000000000000000000000000000000000000000000000000000000000000000000000157





#
# FNV-1a 512 hash on a string
#

def fnv1a_512_str(string):
	
	# Set the offset basis
    hash = FNV1A_512_OFFSET

	# For each character
    for character in string:

		# Xor with the current character
        hash ^= ord(character)

		# Multiply by prime
        hash *= FNV1A_512_PRIME

		# Clamp
        hash &= 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

	# Return the final hash as a number
    return hash
