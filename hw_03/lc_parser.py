import nltk

sentence = "We found that different species and subspecies showed markedly \
different use of howl types, indicating that howl modulation is not arbitrary, \
but can be used to distinguish one population from another.".split()

# Not used because the parser does not terminate.
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

# Not used because the Left Corner Parser doesn't allow grammars with empty
# productions. Does not produce a parser nor a tree.
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

# This grammar produces a decent parse that runs quickly. To do: refine my
# knowledge of grammar and fix the CONJP structure, which is not a real tag.
grammar4 = nltk.CFG.fromstring("""
S -> NP VP NP | NP VP NP VP NP | S CONJP S
NP -> N | NP CC N | ADJ N | ADVP NP | NP PP | N N
VP -> V | V VP |VP CC VP | V ADJP | "to" V | "found" "that"
CONJP -> "indicating" "that"
PP -> P NP
ADVP -> ADV ADJ
ADJP -> ADJ | "not" ADJ
ADV -> "markedly"
ADJ -> "arbitrary," | "different" | "one"
CC -> "but" | "and"
N -> "We" | "subspecies" | "use" | "another." | "howl" | "types," | "modulation" | "species" | "population"
V -> "showed" | "is" | "can" | "be" | "used" | "distinguish"
P -> "of" | "from"
""")

lc_parser = nltk.LeftCornerChartParser(grammar4)
for tree in lc_parser.parse(sentence):
    print tree
