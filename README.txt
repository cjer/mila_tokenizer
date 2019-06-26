MILA tokenizer is licensed by mila@cs.technion.ac.il. I do not own their tokenizer whatsoever.

The run.py script is a simple (and very initial) wrapper calling it through python and creating a YAP compatible tokenized sentences output (one token per line, double linebreak between sentences).

MILA README
===========
Version 1.8 (20130314)

Using the tokenizer
-------------------

java [-Xmx1024m] -jar tokenizer.jar <input> <output>

Example 1: java -Xmx1024m -jar tokenizer.jar file.txt file.xml
Example 2: java -Xmx1024m -jar tokenizer.jar corpus/ corpus_tokenized/

Note: If using the directory mode, the output directory must already exist.
      Try "mkdir corpus_tokenized" before example 2.

