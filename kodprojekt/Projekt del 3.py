import numpy as np

# DNA baser
BASES = ["A", "T", "C", "G"]

def get_random_sequence(n, seed = None):
    
    """
    Returnerar en slumpmässig DNA-sekvens med längden n.

    Parameters
    ----------
    n : int
        Sekvensens längd.
    seed : int, optional
        Slumpfrö som kan användas för reproducerbara resultat.

    Returns
    -------
    str
        En slumpmässig DNA-sekvens.
    """


    np.random.seed(seed)
    rand_ids = np.random.randint(0,4,int(n))
    seq = ''.join([BASES[idx] for idx in rand_ids])
    return seq




def dna_shift_encrypt(seq, key):
    encrypted = []
    for i in range(len(seq)):
        bas = (BASES.index(seq[i]) + key) % 4
        encrypted.append(BASES[bas])
    resultat = "".join(encrypted) #"".join(listans namn) gör att listan omvandlas till en sträng och kopplas till variabeln resultat
        
    return resultat

"""
Returnerar en krypterad DNA-sträng genom att skifta baserna med key steg.

Parameters
----------
seq : str
    Okrypterad DNA-sekvens
key : int
    Antalet steg DNA-baserna skiftas

Returns
-------
str
    Den krypterade DNA-sekvensen
"""



def dna_shift_decrypt(encrypt_seq, key):
    decrypted = []
    for i in range(len(encrypt_seq)):
        bas = (BASES.index(encrypt_seq[i]) - key) % 4
        decrypted.append(BASES[bas])
    resultat2 = "".join(decrypted)
    
    return resultat2
"""
 Returnerar en dekrypterad DNA-sträng som har krypterats genom att skifta baserna med key steg.

 Parameters
 ----------
 encrypt_seq : str
     Krypterad DNA-sekvens
 key : int
     Antalet steg DNA-baserna skiftas

 Returns
 -------
 str
     Den okrypterade DNA-sekvensen
 """
 


def skapa_lista(key_word):
    lista = []
    for x in key_word.upper():
        if x in BASES and x not in lista:
            lista.append(x)
    for x in BASES:
        if x not in lista:
            lista.append(x)
    return lista
"""
Denna funktion skapar en ersättningslista som uppfyller reglerna. 
Den används sedan i funktionerna för encrypt och decrypt. 
"""
def dna_substitution_encrypt(seq, key_word):
    kod = skapa_lista(key_word)
    encrypted = []
    for i in range(len(seq)):
        bas = BASES.index(seq[i])
        encrypted.append(kod[bas])
    resultat = "".join(encrypted)
    return resultat

"""
 Returnerar en krypterad DNA-sträng genom substitution baserad på key_word.

 Parameters
 ----------
 seq : str
     Okrypterad DNA-sekvens
 key_word : str
     Nyckelord som definierar substutitionen

 Returns
 -------
 str
     Den krypterade DNA-sekvensen
 """
   

def dna_substitution_decrypt(encrypt_seq, key_word):
    kod = skapa_lista(key_word)
    decrypted = []
    for i in range(len(encrypt_seq)):
        bas = kod.index(encrypt_seq[i])
        decrypted.append(BASES[bas])
    resultat = "".join(decrypted)
    return resultat
"""
Returnerar en dekrypterad DNA-sträng som har krypterats genom substitution baserad på key_word.

Parameters
----------
encrypt_seq : str
    Krypterad DNA-sekvens
key_word : str
    Nyckelord som definierar substutitionen

Returns
-------
str
    Den okrypterade DNA-sekvensen
"""


def dna_checksum(seq):
    summa = 0
    for i in seq:
        summa += BASES.index(i) + 1
    return summa
"""
Returnerar en kontrollsumma baserad på en DNA-sekvens definierad som 1*antal_A + 2*antal_T + 3*antal_C + 4*antal_G.

Parameters
----------
seq : str
    DNA-sekvens

Returns
-------
int
    Kontrolsumman
"""
    

  
# Denna gjorde vi först

"""def dna_checksum(seq):
    summa = []
    for i in range(len(seq)):
        bas = (BASES.index(seq[i]) + 1)
        summa.append(bas)
    y = sum(summa)
    return y
"""

    


