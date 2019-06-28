# knock_knock.py

# Begins with introducing Knock-knock... 
# Want to hear a Knock-Knock Joke?
# Wait

# knock_knock.py
def error_message(X): 
	if X != ('Who\'s there?'):
		print('You\'re supposed to say "Who\'s there?" Try Again')

def banana(Y):
	if Y != ('Banana who?'):
		print('Nope! You\'re supposed to say Banana Who?')

def orange(O):
	if O != ('Orange who?'):
		print('Wrong again! You\'re supposed to say Orange!')

def stanza1():

	response = input('Knock. Knock. ')
	error_message(response)

	banana_who = input('Banana. ')
	banana(banana_who)

def stanza2():

	response = input('Knock. Knock. ')
	error_message(response)

	orange_who = input('Orange. ')
	orange(orange_who)

	print('Orange you glad I didn’t say banana? ')

def joke(n):

	if n > 1:
		stanza1()
		joke(n-1)

	elif n == 1:
		stanza2()

joke(3)

#def whos_there(L):
	#if L == "Who is there?"
	#	return 