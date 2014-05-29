def transcribe(s):
    '''given a DNA string, replace each T with a U and write it back out as RNA

    (str) -> (str)

    >>>transcribe('ATGCCCGGGTTTAAA')
    AUGCCCGGGUUUAAA

    '''

    RNA = s.replace('T','U')
    
    print(RNA)

#s. replace doesn't actually overwrite the original string s, so have to save it to a new one, RNA.

transcribe('ATTTTTTTTCCCCCCCGGGGGGGG')
    
