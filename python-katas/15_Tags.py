# Create function to turn a given tag and word into an HTML string
# with < > and </i>

def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'

print(make_tags('i', 'Yay'))
