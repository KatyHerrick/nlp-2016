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

sr_parser = nltk.ShiftReduceParser(grammar3, trace=2)
for tree in sr_parser.parse(sentence):
    print tree