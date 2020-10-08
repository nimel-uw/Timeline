#by Nathaniel Imel

import nltk

f = open("in.txt", "r") 
tokens = nltk.word_tokenize( f.read() )
tagged_tokens = nltk.pos_tag(tokens)

period = "."
past = []
present = []
other = []
tenselist = [ past, present, other ]

def make_markers():
    presents = ["VBP", "VBZ", "VBG"]
    tense_markers = [ "VBD", "MD" ]
    for v in presents:
        tense_markers.append(v)
    return tense_markers

#does the sentence contain a tensed item?
def get_marker( pairs ):
    for marker in markers:
        if (marker in pairs):
            return marker

markers = make_markers() # global variable

def get_first_marker(tagged_sent):
    for pairs in tagged_sent: 
        marker = get_marker(pairs)
        if (marker):
            if ( marker in ["VBP", "VBZ", "VBG"] ): 
                return 0
            if (marker == "VBD"):
                return -1
            return -2

#turn list of tuples into a subset list of sentences
def get_sentences():
    sentence_list = []
    current_tag_s = []
    current_sentence = []

    for pairs in tagged_tokens: 

        if ( pairs[1] is period ):
            joined = [item for item in current_sentence]
            joined = " ".join(joined)
            joined = joined + pairs[0]

            sentence_list.append([joined])

            #add the sentence to the correct tense list
            marker = get_first_marker(current_tag_s)
            if ( marker == 0 ):
                present.append(joined)
            elif ( marker == -1 ):
                past.append(joined)
            else: 
                other.append(joined)

            #clear for processing next sentence
            current_tag_s.clear()
            current_sentence.clear()
            continue

        current_sentence.append(pairs[0])
        current_tag_s.append(pairs[1])

    return sentence_list

def truncate_sentences(tenselist):
    get_sentences()
    return [[ (s[:40] + "...") if len(s) > 40 else s for s in item] for item in tenselist] 

tenselist = truncate_sentences(tenselist)
