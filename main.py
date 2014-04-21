import argparse
import sys
import re

from phonebooks import SimpleFilePhonebook as Phonebook

def create(filename):
    try:
        Phonebook.create(filename)
    except IOError:
        print 'Error creating phonebook'

def add(phonebook, name, number):
    phonebook[name] = number

def lookup(phonebook, name):
    try:
        print phonebook[name]
    except KeyError:
        print 'name not found'

def change(phonebook, name, number):
    try:
        phonebook.change(name, number)
    except KeyError:
        print 'name not found'

def reverselookup(phonebook, number):
    print phonebook.reverselookup(number)

def parse_args(args):
    def createable_phonebook(name):
        return name

    def phonebook(name):
        return Phonebook(name)

    def phonenumber(number):
        if not re.match(r'([\-() ]*\d){7,16}', number):
            raise TypeError("%s is not a phone number' % number")
        return number

    parser = argparse.ArgumentParser(prog='phonebook')

    subparsers = parser.add_subparsers()

    def add_phonebook_arg(parser):
        parser.add_argument('-b', '--phonebook', type=phonebook, help='phonebook to use')

    create_parser = subparsers.add_parser('create', help='create a phonebook')
    create_parser.add_argument('filename', type=createable_phonebook, help='filename for phonebook data to be saved')
    create_parser.set_defaults(func=create)

    add_parser = subparsers.add_parser('add', help='look up a phone number')
    add_parser.add_argument('name')
    add_parser.add_argument('number', type=phonenumber)
    add_phonebook_arg(add_parser)
    add_parser.set_defaults(func=add)

    lookup_parser = subparsers.add_parser('lookup', help='look up a phone number')
    lookup_parser.add_argument('name')
    add_phonebook_arg(lookup_parser)
    lookup_parser.set_defaults(func=lookup)

    change_parser = subparsers.add_parser('change', help='look up a phone number')
    change_parser.add_argument('name')
    change_parser.add_argument('number', type=phonenumber)
    add_phonebook_arg(change_parser)
    change_parser.set_defaults(func=change)

    reverselookup_parser = subparsers.add_parser('reverselookup', help='look up a phone number')
    reverselookup_parser.add_argument('name')
    add_phonebook_arg(reverselookup_parser)
    reverselookup_parser.set_defaults(func=reverselookup)

    return parser.parse_args(args)

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    func = args.func
    del args.func
    func(**vars(args))
