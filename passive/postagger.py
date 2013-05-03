#!/usr/bin/env python

"""
Routines for POS tagging with a possibly overkill four-level tagger trained
from the Brown Corpus.
"""

import nltk
from nltk.corpus import brown

from cPickle import dump, load
import sys
import os
from itertools import dropwhile

TAGGER = None

def create_tagger():
    """Train a tagger from the Brown Corpus. This should not be called very
    often; only in the event that the tagger pickle wasn't found."""
    print "Building tagger..."
    train_sents = brown.tagged_sents()

    # These regexes were lifted from the NLTK book tagger chapter.
    t0 = nltk.RegexpTagger(
        [(r'^-?[0-9]+(.[0-9]+)?$', 'CD'), # cardinal numbers
         (r'(The|the|A|a|An|an)$', 'AT'), # articles
         (r'.*able$', 'JJ'),              # adjectives
         (r'.*ness$', 'NN'),              # nouns formed from adjectives
         (r'.*ly$', 'RB'),                # adverbs
         (r'.*s$', 'NNS'),                # plural nouns
         (r'.*ing$', 'VBG'),              # gerunds
         (r'.*ed$', 'VBD'),               # past tense verbs
         (r'.*', 'NN')                    # nouns (default)
        ])
    print "got t0"

    t1 = nltk.UnigramTagger(train_sents, backoff=t0)
    print "got t1"

    t2 = nltk.BigramTagger(train_sents, backoff=t1)
    print "got t2"

    t3 = nltk.TrigramTagger(train_sents, backoff=t2)
    print "Built tagger!"
    return t3

def save_tagger(tagger):
    output = open('tagger.pkl', 'wb')
    dump(tagger, output, -1)
    output.close()

def get_tagger():
    if os.path.exists("tagger.pkl"):
        input = open('tagger.pkl', 'rb')
        tagger = load(input)
        input.close()
        print "The tagger has been loaded from the pickle by Python."
        return tagger
    else:
        tagger = create_tagger()
        save_tagger(tagger)
        return tagger

