# Alexander Dalton

def encode(pswd):  # Encodes password.
    encode_array = []
    encoded_password = ""
    for char in pswd:
        if int(char) == 7:
            encode_array.append("0")
        elif int(char) == 8:
            encode_array.append("1")
        elif int(char) == 9:
            encode_array.append("2")
        else:
            encode_array.append(str(int(char) + 3))
    for num in encode_array:
        encoded_password += num
    return encoded_password

def decode(pswd): # Decodes password
  decoded_array = []
  decoded_password = ""
  for char in pswd:
      if int(char) == 0:
        decoded_array.append("7")
      elif int(char) == 1:
        decoded_array.append("8")
      elif int(char) == 2:
        decoded_array.append("9")
      else:
        decoded_array.append(str(int(char) - 3))

  for num in decoded_array:
    decoded_password += num
  return decoded_password

def main():  # Main Menu Function.
    while True:
        print("Menu\n------------\n1. Encode\n2. Decode\n3. Quit\n")
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            encoded = encode(password)
            print("Your password has been encoded and stored!\n")
        elif choice == 2:
            decoded = decode(encoded)
            print(f"The encoded password is {encoded}, and the original password is {decoded}.\n")
        elif choice == 3:
            break


if __name__ == "__main__":  # Main Code Goes Here.
    main()
