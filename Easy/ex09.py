# Dado uma palavra, imprimir em quais vetores ela aparece.

def FirstOcurrence(haystack, needle):
    if needle not in haystack:
        return False
    
    