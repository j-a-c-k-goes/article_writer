## article title builder ##
utility to build titles for articles. 

# constraints #
article titles should use a colons. 

this is important to beceome split into display and context variants. 

# program flow #
-- get title as input
-- display input
-- confirm if correct input
-- if yes, continue
-- if no, get ready for another input
-- check input for colon character
-- split titles properly and strip unneccesary whitespace
-- bind into correct variables
-- return as an object

# output examples #
title     |----> wormholes: an investigation of internet portals
display   |----> wormholes
context   |----> an investigation of internet portals

title     |----> true and false and none: a quick look @ booleans
display   |----> true and false and none
context   |----> a quick look @ booleans

# to run #
`python3 article_writer.py

# known bugs #
there is a double entry which happens after making corrections to the title.

# updates #
-- define loop to enter multiple titles
-- export titles to csv or txt file
