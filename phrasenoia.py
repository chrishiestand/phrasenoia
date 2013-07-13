#!/usr/bin/env python

__license__= """
    Copyright (c) 2013 Chris Hiestand <https://github.com/chrishiestand>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>."""

import os
import sys
import struct
import random


#You're not paranoid if they really are coming to get you
class PhraseNoia:

    _bytes_needed       = None
    _entropy_count_file = '/proc/sys/kernel/random/entropy_avail'
    _word_list_file     = sys.prefix + "/wordlists/diceware.txt"
    default_numwords    = 5
    random_replace      = 0
    entropy_file        = "/dev/random"
    replacement_chars   = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' \
                          '0123456789,./;\'[]\\`-=<>?:"}{|~!@#$%^&*()_+ '


    def __init__(self, list_file=_word_list_file, entropy_source=entropy_file):
        self._set_list(list_file)
        self._entropy_source = open(entropy_source, "rb")


    def _set_list(self, listfile):
        self._word_list_file = open(listfile, "r")
        self.wordlist        = list(self._word_list_file)
        self._bytes_needed   = (len(self.wordlist).bit_length() + 7) // 8 #round up to bytes


    def _random_bytes(self):
        return self._entropy_source.read(self._bytes_needed)


    def _warn_low_entropy(self):
        if self._entropy_source.name == '/dev/random' and sys.platform.startswith('linux') and \
                os.path.exists('/proc/sys/kernel/random/entropy_avail'):
            f = open(self._entropy_count_file, 'r')
            entropy_count = int(f.read().strip())
            f.close()
            if entropy_count < 500:
                sys.stderr.write('Warning: low system entropy detected. This may take a while.\n' \
                    'Consider increasing entropy or using urandom instead')


    def gen(self, numwords):
        self._warn_low_entropy()
        ids = []
        while len(ids) < numwords:
            tup = struct.unpack("H", self._random_bytes())
            word_id = tup[0]
            #Avoid techniques which result in non-uniform distribution
            #Instead, we skip values outside of the range we want
            #Performance is sacrificed for security
            if word_id >= 0 and word_id < len(self.wordlist):
                ids.append(word_id)
        random_words = [self.wordlist[x].strip() for x in ids]
        phrase = list(' '.join(random_words))
        for r in range(0, self.random_replace):
            replacepos = random.randint(0, len(phrase) - 1)
            phrase[replacepos] = random.choice(self.replacement_chars)
        return ''.join(phrase)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Generate a strong, secure pass phrase",
        usage="%(prog)s number-of-words")
    parser.add_argument(
        '-n', '-numwords',
        dest='numwords',
        metavar='numwords',
        type=int,
        nargs='?',
        default=PhraseNoia.default_numwords,
        help='number of words in the pass phrase [default: %(default)i]')
    parser.add_argument(
        '-w', '-wordlist',
        dest='wordlist',
        metavar='wordlist',
        type=str,
        nargs='?',
        default='diceware.txt',
        help='file: source of words separated by newline [default: %(default)s]')
    parser.add_argument(
        '-s', '--entropy-source',
        dest='entropy_source',
        metavar='entropy_source',
        type=str,
        nargs='?',
        default=PhraseNoia.entropy_file,
        help='file: source of entropy [default: %(default)s]')
    parser.add_argument(
        '-r', '--random-replacements',
        dest='numreplacements',
        metavar='numreplacements',
        type=int,
        nargs='?',
        default=PhraseNoia.random_replace,
        help='number of chars randomly replaced after phrase is created (increases security at the expense of memorization) [default: %(default)i]')
    args = parser.parse_args()

    if not args.numwords or not args.wordlist:
        parser.print_help()
        sys.exit(7)

    phrasegen                 = PhraseNoia(list_file=args.wordlist)
    PhraseNoia.random_replace = args.numreplacements
    print(phrasegen.gen(args.numwords))
    return 0


if __name__ == "__main__":
    sys.exit(main())
