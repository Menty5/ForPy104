from sys import argv
# bonus 3
script, user_name, age = argv
prompt = 'Plese tell me: '

print "Hi %s, I'm the %s script." % (user_name, script)
# bonus 3
print"I'm %s years old." % 19
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print"What kind of computer do you have?"
computer = raw_input(prompt)

print"""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)