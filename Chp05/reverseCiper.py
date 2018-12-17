message = 'Three can keep a secret, if two of them are dead.'
translated = ''

message_dec = ".daed era meht fo owt fi ,terces a peek nac eerhT"


i = len(message_dec) - 1
while i >= 0:
    translated = translated + message_dec[i]
    print(i, message[i], translated)
    i = i - 1
print(translated)