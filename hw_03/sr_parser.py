# Katy Herrick
### NLP—Homework #3
(Resubmitted 3/18/16)

import nltk

sentence = "We found that different species and subspecies showed markedly \
different use of howl types, indicating that howl modulation is not arbitrary, \
but can be used to distinguish one population from another.".split()

# Not used because the parser does not terminate. The final call in the
# trace is R [ S PP NNS CONJP NP VBZ RB JJ CC VBZ VB VB TO VB NP * ].
grammar1 = nltk.CFG.fromstring("""
S -> NP VP | S CONJP S
NP -> PRP | JJ NNS CC NNS | NP PP | JJ NN | NN NN | NN NNS
VP -> VBD RP S | VBD RB NP | VBZ TO VP | VB NP PP
VP -> VB VP | VBZ VP | VBZ RP JJ CC VP
PP -> IN NP | IN NN
CONJP -> "indicating" "that"
PRP -> "We"
VBD -> "found" | "showed"
RP -> "that"
JJ -> "different" | "arbitrary," | "one"
NNS -> "species" | "subspecies" | "types,"
CC -> "and" | "but"
RB -> "markedly" | "not"
NN -> "use" | "howl" | "modulation" | "population" | "another."
IN -> "of" | "from"
VBZ -> "is" | "can"
VB -> "used" | "distinguish" | "be"
TO -> "to"
""")

# Not used because it is too simplistic. However, it does
# run and generate a tree with just one branch!
grammar2 = nltk.CFG.fromstring("""
S -> NP VP
NP -> "We"
VP -> "found" "that" "different" "species" "and" "subspecies" "showed" "markedly" \
"different" "use" "of" "howl" "types," "indicating" "that" "howl" "modulation" \
"is" "not" "arbitrary," "but" "can" "be" "used" "to" "distinguish" "one" \
"population" "from" "another."
""")

# Not used because creating the parser throws warnings such as
# "Warning: VP -> V will never be used".
# Shift-reduce moves from right to left, so a right grammar should be used.
grammar3 = nltk.CFG.fromstring("""
S -> NP VP NP VP NP | NP VP CC VP VP NP IN NP| S CONJP S
NP -> N | N CC N | ADVP NP | N IN NP | "howl" "types," | "howl" "modulation" | \
"one" "population" | "another."  | "not" "arbitrary,"
VP -> V | "to" V | V ADJP | V VP | "found" "that" | "be" "used" |
CONJP -> "indicating" "that"
ADVP -> "markedly" "different"
N -> "We" | "different" "species" | "subspecies" | "use"
V -> "showed" | "distinguish" | "is" | "can"
CC -> "and" | "but"
IN -> "from" | "of"
ADJP -> "not" "arbitrary,"
""")

# This produces a parse, though it does not fully align with the rules of
# semantic units. In particular, it categorizes "We found that different
# species and subspecies" incorrectly as a sentence. Due to the lack of
# backtracking in nltk's ShiftReduceParser algorithm, rules have to be made
# oddly specific or else it doesn't produce a parse at all.
grammar4 = nltk.CFG.fromstring("""
S -> S VP NP | NP VP NP | S CONJP S
NP -> "We" | "different" "species" "and" "subspecies" | "markedly" \
"different" "use" "of" "howl" "types," | "howl" "modulation" | \
"one" "population" "from" "another."
VP -> VP CC VP | "found" "that" | "showed" | \
"is" "not" "arbitrary," | "can" "be" "used" "to" "distinguish"
CONJP -> "indicating" "that"
CC -> "but"
""")

sr_parser = nltk.ShiftReduceParser(grammar4)
for tree in sr_parser.parse(sentence):
    print tree
