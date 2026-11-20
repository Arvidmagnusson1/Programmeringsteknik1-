

import numpy as np
# DNA baser
BASES = ["A", "T", "C", "G"]
def get_random_sequence(n, seed = None):
    np.random.seed(seed)
    rand_ids = np.random.randint(0,4,int(n))
    seq = ''.join([BASES[idx] for idx in rand_ids])
    return seq

def dna_shift_encrypt(seq, key):
    result = ""
    for bas in seq:
        ny_index = (BASES.index(bas)+key) % 4
        result += BASES[ny_index]
    return result

   
def dna_shift_decrypt(encrypt_seq, key):
    result = ""
    for bas in encrypt_seq:
        ny_index = (BASES.index(bas)-key) % 4
        result += BASES[ny_index]
    return result
    

def dna_substitution_encrypt(seq, key_word):
    key_word = key_word.upper()
    ersattning = ""
    for bokstav in key_word:
        if bokstav in BASES and bokstav not in ersattning:
            ersattning += bokstav
    for bokstav in BASES:
        if bokstav not in ersattning:   
            ersattning += bokstav
    result = ""
    for bokstav in seq:
        position = BASES.index(bokstav)
        result += ersattning[position]  
    return result
            
        

   
def dna_substitution_decrypt(encrypt_seq, key_word):
    key_word = key_word.upper()
    ersattning = ""
    for bokstav in key_word:
        if bokstav in BASES and bokstav not in ersattning:
            ersattning += bokstav
    for bokstav in BASES:
        if bokstav not in ersattning:   
            ersattning += bokstav
    result = ""
    for bokstav in encrypt_seq:
        position = ersattning.index(bokstav)
        result += BASES[position]
    return result
    
        

    
   
def dna_checksum(seq):
    b
  
