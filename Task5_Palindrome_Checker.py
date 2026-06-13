text = input("Enter a word: ")
reverse_text = ""
for ch in text:
    reverse_text = ch + reverse_text
if text == reverse_text:
    print("Palindrome")
else:
    print("Not a Palindrome")