from sys import argv
script,filename=argv
prompt = ">"
txt=open(input(prompt))
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()
