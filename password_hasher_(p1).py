import hashlib
def dictionary_attack(password_hash):
    dictionary = ['letmein','password','12345','football']
    password_found = False
    for dictionary_value in dictionary
    hashed_value = (hashlib.md5(dictionary_value)).hexdigest()
    if hashed_value == password_hash:
        password_found = True
        recovered_password = dictionary_value


    if password_found == True:
        print ('Found match for hashed value \n'),password_hash
        print ('Password recovered: '),recovered_password
    else:
        print ('password was not found')

def main():
    password_hash = rav_input ('Enter hashed value: ')
    dictionary_attack(password_hash)

if __name__ == '__main__':
    main()
