########
PROBLEM
########

The code you will write is based on the “Caesar Cipher” where each letter is shifted a certain number of places left or right through the alphabet. The alphabet is treated as being circular so that the first letter follows after the last letter, and the last letter precedes the first letter.  These ideas will be applied separately to uppercase letters, lower case letters, and digits. For example, with a shift of 1, ‘A’ becomes ‘B’, ‘Z’ becomes ‘A’, ‘a’ becomes ‘b’, ‘z’ becomes ‘a’, ‘0’ becomes ‘1’, ‘9’ becomes ‘0’. Spaces, punctuation, and any other symbols are unaffected in this scheme. Your task is to write a function to encrypt a string using this Caesar Cipher. 

INPUT FORMAT
Your function will take an input string that begins with a number representing the shift. The number will be in the range -1000000000 to 1000000000 (negative 1 billion to 1 billion). The number is followed by a colon (‘:’). The rest of the line consists of a string of 1 to 200 arbitrary characters and represents a fragment of the text to be encrypted.
 
OUTPUT FORMAT
Output will be the corresponding encrypted text fragment
  
SAMPLE INPUT:
1:some text
 
SAMPLE OUTPUT:
tpnf ufyu
