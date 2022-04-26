"""
	need to build a title for articles 

	article titles should use a colons.
	and become split into display and context variants 

	- - - example - - -
	title 	|----> wormholes: an investigation of internet portals
	display	|----> wormholes
	context	|----> an investigation of internet portals

	title 	|----> true and false and none: a quick look @ booleans
	display	|----> true and false and none
	context	|----> a quick look @ booleans

	- - - program flow - - -
	get title as input
	display input
	confirm if correct input
	if yes, continue
	if no, ready for another input
	check input for colon character
	split titles poperly and strip unneccesary whitespace
	bind into correct variables
	return as an object
"""

def make_title():
	# - - - state what the prgram is doing - - -
	print("- - - make a title for your article - - -")
	# - - - define bool to control loop - - -
	making_title = True
	# - - - bind special character to variable - - -
	special_character = ":"
	# - - - run while loop until false - - -
	while making_title:
		try:
			# - - - bind prompt to title variable - - -
			article_title = str(input("enter the article title: "))
			# - - - check for special character - - -
			while special_character not in article_title:
				# - - - print correction statement  - - -
				print("- - - titles must use a colon. correct entry to proceed. - - -")
				# - - - reprompt and rebind - - - 
				article_title = str(input("enter colon-corrected article title: "))
			# - - - display input - - -
			print(article_title)
			# - - - confirm is pnput is intended - - -
			confirm = str(input("confirm this is the title to be used (use y or n ): "))
			# - - - confirm is "n" - - -
			if confirm.lower() == "n":
				# - - - print correction statement - - - 
				print("- - - update title below - - -")
				# - - - reprompt and rebind - - - 
				article_title = str(input("enter intended article title: "))
			# - - - confirm is "y" - - -
			else: 
				# - - - print update - - -
				print(f"'{article_title}' is valid.")
				# - - - split the title @ the colon - - -
				split_article_title = article_title.split(":")
				# - - - make the display title from first element in list - - -
				make_display_title = split_article_title[0].strip()
				# - - - make the context title from second element in list - - -
				make_context_title = split_article_title[1].strip()
				# - - - return variables as object - - -
				return {
					'full_title': article_title, 
					'display_title': make_display_title,
					'context_title': make_context_title,
					}
				# - - - end the loop - - -
				making_title = False

		except ValueError:
			print("- - - please input a valid string/text input using a colon - - -")

# - - - on run and module import - - -
if __name__ == "__main__":
	titles = []
	title = make_title()
	titles.append(title)
	print(titles)


