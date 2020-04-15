import hashlib

def sha1_hash(input_str):
    
    hash_obj = hashlib.sha1(input_str.encode())
    hash_value = hash_obj.hexdigest()
    return hash_value


wecode_hash_value = sha1_hash('wecode')
print(wecode_hash_value)
print(len(wecode_hash_value))

hash_value_1234 = sha1_hash('1234')
print(hash_value_1234)
print(len(hash_value_1234))