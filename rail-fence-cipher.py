
'''
Implement the rail-fence cipher. Both encryption and decryption should be written. These functions will both take a an input string, and an integer that represents the encryption/decryption key.

Example: 

ENCRYPTION: Given a number (we'll choose 3), visualize a zig-zag with that height (in this case, 3 lines high.) Let's say our message is BAILEYDOGISREALLYCOOL. This looks like:
BAILEYDOGISREALLYCOOL
B   E   G   E   Y   L
 A L Y O I R A L C O
  I   D   S   L   O
See how it goes up and down? Now, to get the ciphertext, instead of reading with the zigzag, just read along the lines instead.

The top line has BEGEYL, the second line has ALYOIRALCO and the last line has IDSLO.

Putting those together gives you BEGEYLALYOIRALCOIDSLO, which is the ciphertext.



DECRYPTION: Given the same encryption key/number and a cipher text, return the decrypted result. For example, with the most recently produced ciphertext BEGEYLALYOIRALCOIDSLO:
decrypt("BEGEYLALYOIRALCOIDSLO", 3) = "BAILEYDOGISREALLYCOOL"


Ex:
encrypt("THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG", 4) = TCNMRZHIKWFUPETAYEUBOOJSVHLDGQRXOEO
encrypt("BAILEYDOGISREALLYCOOL", 3) = BEGEYLALYOIRALCOIDSLO
encrypt("ANTIDISESTABLISHMENTARIANISM", 5) = ASMNNETHEAITSASNISIIBITRMDLA

decrypt("TCNMRZHIKWFUPETAYEUBOOJSVHLDGQRXOEO", 4) = "THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG"
decrypt("BEGEYLALYOIRALCOIDSLO", 3) = "BAILEYDOGISREALLYCOOL"
decrypt("ASMNNETHEAITSASNISIIBITRMDLA", 5) = "ANTIDISESTABLISHMENTARIANISM"
'''
global_obj = {}
def encrypt(string, key):
    obj = {}
    for i in range(1, key + 1):
      obj[i] = ''
        
    j = 0
    direction = 'down'
    while j < len(string):
      if j == 0: 
        for i in range(1, key + 1):
          if j < len(string):
            obj[i] += string[j]
          j += 1
        direction = 'up'
      else:
        for i in range(1, key):
          if direction == 'down':
            real_index = i + 1
          else:
            real_index = key - i
          if j < len(string):
            obj[real_index] += string[j]
          j += 1
        if direction == 'down':
          direction = 'up'
        else:
          direction = 'down'
            
    master_string = ''
    for i in range(1, key + 1):
        master_string += obj[i]
        global_obj[i] = len(obj[i])
    print(master_string)
  
def decrypt(string, key):
  local_obj = {}
  start_index = 0
  decrypted_string = ''
  for i in range(1, key + 1):
    length = global_obj[i]
    substring = string[start_index:start_index+length]
    local_obj[i] = substring
    start_index += length
  j = 0
  while j < len(string):
    if j == 0: 
      for i in range(1, key + 1):
        if j < len(string):
          decrypted_string += local_obj[i][0]
          local_obj[i] = local_obj[i][1:]
        j += 1
      direction = 'up'
    else:
      for i in range(1, key):
        if direction == 'down':
          real_index = i + 1
        elif direction == 'up':
          real_index = key - i

        if j < len(string):
          decrypted_string += local_obj[real_index][0]
          local_obj[real_index] = local_obj[real_index][1:]
        j += 1
      if direction == 'down':
        direction = 'up'
      else:
        direction = 'down'
  print(decrypted_string)

encrypt("BAILEYDOGISREALLYCOOL", 3)
decrypt("BEGEYLALYOIRALCOIDSLO", 3)

encrypt("ANTIDISESTABLISHMENTARIANISM", 5)
decrypt("ASMNNETHEAITSASNISIIBITRMDLA", 5)

encrypt("THEQUICKBROWNFOXJUMPSOVERTHELAZYDOG", 4)
decrypt("TCNMRZHIKWFUPETAYEUBOOJSVHLDGQRXOEO", 4)



    

