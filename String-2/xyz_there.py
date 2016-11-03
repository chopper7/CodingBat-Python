# Coding Bat / Python / String-2 / "xyz_there"
# URL -- http://codingbat.com/prob/p149391

"""
Return True if the given string contains an appearance of "xyz" where
the xyz is not directly preceeded by a period (.). So, "xxyz" counts but
"x.xyz" does not.
xyz_there('abc.xyzxyz') → True
xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
"""

def xyz_there(str):
    working_str = str.replace('.xyz', '')
    return 'xyz' in working_str
