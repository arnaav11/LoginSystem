def Caeser_Cipher(string: str, Shift: int = 7):

    """
    Converts given string into encrypted string with the caeser cipher method.

    string (str) -> input string
    Shift (int) -> shift number to be used

    """

    text_ciphered = ''


    for i in string:
        text_ciphered += chr(ord(i)+Shift)

    return(text_ciphered)


def deCaeser_Cipher(string: str, Shift: int = 7):

    """
    decrypts a string encrypted using caeser cipher, given the shift number.

    string (str) -> encrypted string
    Shift (int) -> shift number
    
    """

    text_deciphered = ''

    for i in string:
        text_deciphered += chr(ord(i) - Shift)


    return(text_deciphered)