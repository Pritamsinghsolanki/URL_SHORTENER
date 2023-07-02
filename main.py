import pyshorteners

link=input("Enter the link")
shortener=pyshorteners.Shortener()

a=shortener.tinyurl.short(link)

print(a)