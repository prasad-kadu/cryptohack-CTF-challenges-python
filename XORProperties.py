# Using the properties to undo the encryption
KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2_KEY1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_KEY3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_AND_KEYS = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

DKEY1 = bytes.fromhex(KEY1)
DKEY2_KEY1 = bytes.fromhex(KEY2_KEY1)
DKEY2_KEY3 = bytes.fromhex(KEY2_KEY3)
DFLAG_AND_KEYS = bytes.fromhex(FLAG_AND_KEYS)

DKEY3 = []

for i in range(len(DKEY2_KEY1)):
    result_xor = DKEY2_KEY1[i] ^ DKEY2_KEY3[i]
    DKEY3.append(result_xor)

print(bytes(DKEY3))

DFLAG = []

for i in range(len(DFLAG_AND_KEYS)):
    result_xor = DFLAG_AND_KEYS[i] ^ DKEY1[i] ^ DKEY3[i] ^ DKEY2_KEY1[i]
    DFLAG.append(result_xor)

print(bytes(DFLAG))