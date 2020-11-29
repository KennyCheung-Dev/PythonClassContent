# Main Code
# Will need a 2d list as the storage
# which eventually looks like this:
# Let's say key is ACT
# Message is BANANA & PEEL  ->  BANANAPEEL

# Step 1, create the structure
# ACT = 3 columns of storage
#[[], [], []]
# TRICKY = 6 columns
#[[], [], [], [], [], []]

# Step 2: Put content into storage
# Loop between the 3, or 6 columns, and distribute letter content in one by one
#[[BAPL], [ANE], [NAE]]

# Step 3: Encrypt the message inside based on the key
# ACT   ->   0, 2, 19
# [[BAPL], [ANE], [NAE]]
# BAPL -> BAPL
# ANE -> CPG
# NAE -> ???

# Step4: Extract the result from the storage, into a complete String
# Reverse process of step 2
#[[BAPL], [ANE], [NAE]] -> BANANAPEEL

# Step5: print!

# Helper functions

# Functions StripSymbols(content)
# this one stakes away all spaces, symbols and only leave the letters

# Functions PositionToString(i)
# This one transform   0 to A,    or    1 to B,    or    2 to C

# Functions String to Position(letter)
# This one transform A to 0 ,    B to 1,   C to 2