
# f = open('newfile.txt', 'w') 'w' changes, 'a' appends
# f.write("And this is some added text\n")
# f.close()


f = open('newfile.txt', 'a')
lines = ['Hello', 'World', 'Welcome', 'To', 'File_IO']
text = '\n'.join(lines)
f.writelines(text)
f.close()
