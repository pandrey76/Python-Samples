# Python3 program to validate
# GUID (Globally Unique Identifier)
# using regular expression
import re


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
str1 = "123e4567-e89b-12d3" + "-a456-9AC7CBDCEE52"
print(isValidGUID(str1))

# Test Case 2:
str2 = "{123e4567-e89b-12d3-" + "a456-9AC7CBDCEE52}"
print(isValidGUID(str2))

# Test Case 3:
str3 = "123e4567-h89b-12d3-a456" + "-9AC7CBDCEE52"
print(isValidGUID(str3))

# Test Case 4:
str4 = "123e4567-h89b-12d3-a456"
print(isValidGUID(str4))

# This code is contributed by avanitrachhadiya2155
