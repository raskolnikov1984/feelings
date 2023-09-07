from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize

cadena_ejemplo = """
Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult."""

sent_tokenize(cadena_ejemplo)

# Retorna, Tokenizar por oración.
"""
["\nMuad'Dib learned rapidly because his first training was in how to learn.",
 'And the first lesson of all was the basic trust that he could learn.',
 "It's shocking to find how many people do not believe they can learn,\nand how
 many more believe learning to be difficult."]
"""

# Retorna, Tokenizar por palabra.

"""
["Muad'Dib",
 'learned',
 'rapidly',
 'because',
 'his',
 'first',
 'training',
 'was',
 'in',
 'how',
 'to',
 'learn',
 '.',
 'And',
 'the',
 'first',
 'lesson',
 'of',
 'all',
 'was',
 'the',
 'basic',
 'trust',
 'that',
 'he',
 'could',
 'learn',
 '.',
 'It',
 "'s",
 'shocking',
 'to',
 'find',
 'how',
 'many',
 'people',
 'do',
 'not',
 'believe',
 'they',
 'can',
 'learn',
 ',',
 'and',
 'how',
 'many',
 'more',
 'believe',
 'learning',
 'to',
 'be',
 'difficult',
 '.']
"""

# Cita de Worf
worf_quote = "Sir, I protest. I am not a merry man!"
words_in_quote = word_tokenize(worf_quote)

# Retorna
"""
['Sir', ',', 'I', 'protest', '.', 'I', 'am', 'not', 'a', 'merry', 'man', '!']
"""

stop_words = set(stopwords.words("english"))
filtered_list = []

# Ciclo for exhaustivo
"""
for word in words_in_quote:
        if word.casefold() not in stop_words:
                filtered_list.append(word)
"""
# List comprenhension
filtered_list = [
    word for word in words_in_quote if word.casefold() not in stop_words
]

# Palabras en filtered_list
"""
['Sir', ',', 'protest', '.', 'merry', 'man', '!']
"""
