# Python3 program to validate
# GUID (Globally Unique Identifier)
# using regular expression
import re
import uuid
import struct

# Function to validate GUID
# (Globally Unique Identifier)
def isValidGUID(str):
    # Regex to check valid
    # GUID (Globally Unique Identifier)
    regex = "^[{]?[0-9a-fA-F]{8}" + "-([0-9a-fA-F]{4}-)" + "{3}[0-9a-fA-F]{12}[}]?$"

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if (str == None):
        return False

    # Return if the string
    # matched the ReGex
    if (re.search(p, str)):
        return True
    else:
        return False


# Driver code

# Test Case 1:
# str1 = "123e4567-e89b-12d3" + "-a456-9AC7CBDCEE52"
# print(isValidGUID(str1))

# Test Case 2:
# str2 = "{123e4567-e89b-12d3-" + "a456-9AC7CBDCEE52}"
# print(isValidGUID(str2))

# Test Case 3:
# str3 = "123e4567-h89b-12d3-a456" + "-9AC7CBDCEE52"
# print(isValidGUID(str3))

# Test Case 4:
# str4 = "123e4567-h89b-12d3-a456"
# print(isValidGUID(str4))

# This code is contributed by avanitrachhadiya2155

def get_correct_hex_byte_string(value) -> str:
    """

    :param value:
    :return:
    """
    if len(str(value)) % 2 != 0:
        return '0' + str(value)
    return str(value)


class GuidConverter:
    """

    """

    def __init__(self, guid_string: str):
        """

        :param guid_string:
        """
        pattern = re.compile(
            r'{' +
            r'\s*0[xX]([0-9a-fA-F]{8}),' +
            r'\s*0[xX]([0-9a-fA-F]{4}),' +
            r'\s*0[xX]([0-9a-fA-F]{4}),' +
            r'\s*'
            r'{' +
            r'\s*0[xX]([0-9a-fA-F][0-9a-fA-F]?),' +
            r'\s*0[xX]([0-9a-fA-F][0-9a-fA-F]?),' +
            r'\s*0[xX]([0-9a-fA-F][0-9a-fA-F]?),' +
            r'\s*0[xX]([0-9a-fA-F][0-9a-fA-F]?),' +
            r'\s*0[xX]([0-9a-fA-F][0-9a-fA-F]?),' +
            r'\s*0[xX]([0-9a-fA-F][0-9a-fA-F]?),' +
            r'\s*0[xX]([0-9a-fA-F][0-9a-fA-F]?),' +
            r'\s*0[xX]([0-9a-fA-F][0-9a-fA-F]?)' +
            r'\s*' +
            r'}' +
            r'\s*' +
            r'}'
        )
        m1 = pattern.search(guid_string)
        if m1 is None:
            raise NotImplementedError("Error parsing string containing guid.")
        temp_string = m1[1] + m1[2] + m1[3] + m1[4] + m1[5] + m1[6] + m1[7] + m1[8] + m1[9] + m1[10] + m1[11]
        # print(temp_string)
        self.__guid_groups = [
            get_correct_hex_byte_string(m1[1]),
            get_correct_hex_byte_string(m1[2]),
            get_correct_hex_byte_string(m1[3]),
            get_correct_hex_byte_string(m1[4]) + \
            get_correct_hex_byte_string(m1[5]) + \
            get_correct_hex_byte_string(m1[6]) + \
            get_correct_hex_byte_string(m1[7]) + \
            get_correct_hex_byte_string(m1[8]) + \
            get_correct_hex_byte_string(m1[9]) + \
            get_correct_hex_byte_string(m1[10]) + \
            get_correct_hex_byte_string(m1[11])
        ]

        temp_string = self.__guid_groups[0] + self.__guid_groups[1] + self.__guid_groups[2] + self.__guid_groups[3]
        # print(temp_string)
        self.__internal_uuid = uuid.UUID(temp_string)

    def get_guid_as_int(self):
        """

        :return:
        """
        # converted_result = int(self.__guid_groups[0], 16)

        # print(int(self.__guid_groups[0], 16))
        # print(int(self.__guid_groups[1], 16))
        # print(int(self.__guid_groups[2], 16))
        result_pack = struct.pack('>IHH',
                                  int(self.__guid_groups[0], 16),
                                  int(self.__guid_groups[1], 16),
                                  int(self.__guid_groups[2], 16))

        result_string = ""
        result_unpack = struct.unpack('IHH',  result_pack)
        # print(result_unpack)
        for i in result_unpack:
            result_string += format(i, 'x')
        result_string += self.__guid_groups[3]
        return result_string

# Converting to big endian hex string
# //////////////////////////////////////////////////////////////////////////

# converted_result = int(hex_string, 16)
# print(converted_result)
# 947156929
# print(converted_result.to_bytes(4, 'big'))
# b'8tw\xc1'
# import struct
# print(struct.pack('>I', converted_result))
# b'8tw\xc1'
# print(hex(struct.unpack('I', struct.pack('>I', converted_result))[0]))
# 0xc1777438
# print(format(struct.unpack('I', struct.pack('>I', converted_result))[0], 'x'))
# c1777438

# //////////////////////////////////////////////////////////////////////////
