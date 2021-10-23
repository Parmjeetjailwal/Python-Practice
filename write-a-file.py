text = "Hello sir\nThis is your key card sir \nHave a nice day!\n"

with open("test.txt",'w') as file:   # content of text variable add to a file text.txt which is created in present working directory
    file.write(text)

# text = "This text is appended in text.txt file"

# with open("test.txt",'a') as file:   # content of text variable appended to a file text.txt 
#     file.write(text)