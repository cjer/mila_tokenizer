# Author: Dan Bareket

from tempfile import NamedTemporaryFile
import sys
from lxml import etree
import subprocess
import os

def run_tokenizer_on_text(text, use_tempfile=False, temp_input_path='temp_input.txt', temp_output_path='temp_output.xml'):
    if use_tempfile:
        temp_input_file = NamedTemporaryFile(mode='w', encoding='utf8', delete=False)
        temp_input_file.write(text)
        print (temp_input_file.name)
        temp_input_path = temp_input_file.name
    else:
        with open(temp_input_path, 'w', encoding='utf8') as temp_input_file:
            temp_input_file.write(text)
    temp_output_path = run_tokenizer_on_file(input_path, output_path)
    return temp_output_path

def run_tokenizer_on_file(input_path, output_path='temp_output.xml', tokenizer_path=None):
    if tokenizer_path is None:
        tokenizer_path = 'tokenizer.jar'
    subprocess.call(['java', '-Xmx1024m', '-jar', tokenizer_path, input_path, output_path])
    return output_path


def create_tokenized_sentences(mila_xml_path, output_path):
    root = etree.parse(mila_xml_path)
    sents = []
    for s in root.xpath('//sentence'):
        sl = [t.attrib['surface'] for t in s.xpath('./token')]
        sents.append(sl)

    with open(output_path, 'w', encoding='utf8') as f:
        for s in sents:
            for w in s:
                f.write(w)
                f.write('\n')
            f.write('\n')

if __name__ == '__main__':
    
    if len(sys.argv)<2 or len(sys.argv)>3:
        print (f"Usage: {sys.argv[0]} <input_path> [<output_path>]\n# output_path default: <input_path>.tokenized.txt")
    else:
        input_path = sys.argv[1]
        if len(sys.argv)==3:
            output_path = sys.argv[2]
        else:
            output_path = input_path+'.tokenized.txt'

        print("Running MILA Tokenizer...")
        temp_xml_path = run_tokenizer_on_file(input_path)
        print("Finished")
        print(f"Extracting tokens and writing output file: {output_path}")
        create_tokenized_sentences(temp_xml_path, output_path)
        print("Finished") 
        print("Deleting MILA xml file...")               
        os.remove(temp_xml_path)
        print("Done. Have a good day :)")
