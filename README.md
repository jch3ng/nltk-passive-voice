[![Build Status](https://travis-ci.org/j-c-h-e-n-g/nltk-passive-voice.png)](https://travis-ci.org/j-c-h-e-n-g/nltk-passive-voice)

## About
wefwef to trigger build?
`copied from http://narorumo.googlecode.com in late April 2013`

> First pass at finding passive voice sentences, and more
> importantly, getting familiar with NLTK.

> Tags a sentence with a way-overkill four-level tagger trained from the Brown
> Corpus, and then looks at its verbs. If somewhere in the sentence, there's a
> to-be verb and then later on a non-gerund, we'll flag the sentence as probably
> passive voice.

> Developed against NLTK 2.0b5.

## Why

This was just minimal NLTK tinkering from April 2013 and may continue. 

This particular code detects if it's passive voice - I'd like to inject it for the lulz. Original goal was to make something to inject passive voice into academic papers or any sort of offical documentation. This doesn't do it, but is nonetheless interesting enough to tinker & experiment & learn with.


## Usage

your first run will build out the tagger:
```
$ python passive.py
Building tagger...
got t0
got t1
got t2
Built tagger!
```

... which will create `tagger.pkl`, around 1.3MB in size. Subsequent runs will load the tagger. Do something like this: 

```
$ cat passive.txt  | python passive.py
The tagger has been loaded from the pickle by Python.
passive: If the model has succeeded in extracting all the "signal" from the data, there should be no pattern at all in the errors: the error in the next period should not be correlated with any previous errors, and the bars on the autocorrelation plot therefore should all be close to the zero line. 
passive: my shit was eaten by you. 
passive: I was curious why my windows were all immediately getting maximized on my new
passive: Applications. A program called Maximus is included by UNR. To make the behavior
passive: Maximus from that list. Problem solved! Why was the road crossed by the
passive: chicken? The problem was solved. The can had been opened.
passive: window manager setting. The TV was being stared at by the cat. It was moved by
passive: Every valley shall be exalted, and every mountain and hill shall be made low;
passive: and the crooked shall be made straight, and the rough places plain.
passive: Now is the winter of our discontent Made glorious summer by this sun of York.
passive: Never in the field of human conflict was so much owed by so many to so few.
passive: In general, the passive voice should be used when the receiver of the action is
passive: The child was struck by the car.
passive: The store was robbed last night.
passive: Plows should not be kept in the garage.
passive: Kennedy was elected president.
passive: My remarks have been grossly distorted in the press.
passive: The breakthrough was achieved by Burlingame and Evans, two researchers in the
passive: We had hoped to report on this problem but the data was inadvertently deleted
passive: The passive voice is often used in scientific writing because of the tone of
```
