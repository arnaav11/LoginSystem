def Caeser_Cipher(string: str, Shift: int = 7):

    """
    Converts given string into encrypted string with the caeser cipher method.

    string (str) -> input string
    Shift (int) -> shift number to be used

    """

    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ALPHABETS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    text_ciphered = ''

    alpha_found = False
    for i in string:
        for ii,jj in enumerate(alphabets):
            global alpha_updated
            if i == jj and alpha_found == False and i.lower() == i:
                alpha_found = True
                alpha_updated = alphabets[ii + Shift]
            elif  i == jj.upper() and alpha_found == False and i.upper() == i:
                alpha_found = True
                alpha_updated = ALPHABETS[ii + Shift]

            
            
        if alpha_found == True:
                text_ciphered += alpha_updated
        else:
            text_ciphered += i

        alpha_found = False

    return(text_ciphered)


def deCaeser_Cipher(string: str, Shift: int = 7):

    """
    decrypts a string encrypted using caeser cipher, given the shift number.

    string (str) -> encrypted string
    Shift (int) -> shift number
    
    """

    text_deciphered = ''

    alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    ALPHABETS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    alpha_found = False
    for i in string:
        for ii,jj in enumerate(alphabets):
            global alpha_updated
            if i == jj and alpha_found == False and i.lower() == i:
                alpha_found = True
                alpha_updated = alphabets[ii - Shift]
            elif  i == jj.upper() and alpha_found == False and i.upper() == i:
                alpha_found = True
                alpha_updated = ALPHABETS[ii - Shift]

            
            
        if alpha_found == True:
                text_deciphered += alpha_updated
        else:
            text_deciphered += i

        alpha_found = False


    return(text_deciphered)