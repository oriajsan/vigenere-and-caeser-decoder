alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decodeCharCaesar(char, num):
  index = 0
  for i in range(0, len(alphabet)):
    if char == alphabet[i]:
      index = i
      break
  index -= num
  while index > len(alphabet) - 1:
    index -= len(alphabet) - 1
  return alphabet[index]

def decodeTextCaesar(text, num):
  translate = ""
  for i in range(len(text)):
    if text[i] not in alphabet:
      translate += text[i]
    else:
      char = decodeCharCaesar(text[i], num)
      translate += char
  return translate

def decodeCharVigenere(char, word):
  startOfNewAlphabet = ""
  endOfNewAlphabet = ""
  for i in range(len(alphabet)):
    if alphabet[i] == word:
      indexWord = i
      break
  for i in range(len(alphabet)):
    if i < indexWord:
      endOfNewAlphabet += alphabet[i]
    else:
      startOfNewAlphabet += alphabet[i]
  startOfNewAlphabet += endOfNewAlphabet
  for i in range(len(startOfNewAlphabet)):
    if char == startOfNewAlphabet[i]:
      indexChar = i
      break
  return alphabet[indexChar]

def decodeTextVigenere(text, word):
  translate = ""
  counter = 0
  for i in range(len(text)):
    if text[i] not in alphabet:
      if text[i] == " ":
        translate += text[i]
      else:
        translate += text[i]
        counter += 1
        if counter >= len(word):
          counter = 0
    else:
      char = decodeCharVigenere(text[i], word[counter])
      translate += char
      counter += 1
      if counter >= len(word):
        counter = 0
  return translate

def menu():
  print("|" + ("-" * 36) + "|")
  print("|" + (" " * 5) + "CESAR AND VIGENERE DECODER" + (" " * 5) + "|")
  print("|" + (" " * 12) + "by Oriajsan" + (" " * 13) + "|")
  print("|" + ("-" * 36) + "|")
  print("|Options:" + (" " * 28) + "|")
  print("|[0] - Decode in Caesar" + (" " * 14) + "|")
  print("|[1] - Decode in Vigenre" + (" " * 13) + "|")
  print("|[2] - Decode with both together" + (" " * 5) + "|")
  print("|" + ("-" * 36) + "|")

def main():
  answer = -1

  while answer == -1:
    menu()
    print("Press the number of option: ")
    answer = int(input())
    if answer == 0:
      print("[Choosen Caesar!]")
      print("Enter the text to be decoded: ")
      text = str(input())
      print("Enter the decoding number: ")
      number = int(input())
      print(decodeTextCaesar(text, number))
      break
    elif answer == 1:
      print("[Choosen Vigenere!]")
      print("Enter the text to be decoded: ")
      text = str(input())
      print("Enter the decoding word: ")
      word = str(input())
      print(decodeTextVigenere(text, word))
      break
    elif answer == 2:
      print("[Both choose!]")
      print("Enter the text to be decoded: ")
      text = str(input())
      print("Enter the decoding number: ")
      number = int(input())
      print("Enter the decoding word: ")
      word = str(input())
      print(decodeTextCaesar(decodeTextVigenere(text, word), number))
      break
    else:
      answer = -1
      print("Option off the menu, please check again...")

main()