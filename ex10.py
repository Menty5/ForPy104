tabby_cat = "\tI'm %s in." % "tabbed"
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
# bonus3 4
fat_cat = '''
I'll do a list:
\t* %r 
\t* %s
\t* Catnip\n\t* Glass
''' % ("Cat food", "Fishies")

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" % i,