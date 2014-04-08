import argparse
import sys

def create(filename):
    print 'creating phonebook at', filename

def add(phonebook, name, number):
    print 'adding', name, number, 'to', phonebook

def lookup(phonebook, name):
    print 'looking up', name, 'in', phonebook

def change(phonebook, name, number):
    print 'changing', name, 'in', phonebook, 'to', number

def reverselookup(phonebook, number):
    print 'looking up', number, 'in', phonebook

def parse_args(args):
    def createable_phonebook(name):
        return name

    def phonebook(name):
        return [name]

    def phonenumber(number):
        return number

    parser = argparse.ArgumentParser(prog='phonebook')

    subparsers = parser.add_subparsers()

    def add_phonebook_arg(parser):
        parser.add_argument('-b', '--phonebook', type=phonebook, help='the phonebook')

    create_parser = subparsers.add_parser('create', help='create a phonebook')
    create_parser.add_argument('filename', type=createable_phonebook, help='adsf')
    create_parser.set_defaults(func=create)

    add_parser = subparsers.add_parser('add', help='look up a phone number')
    add_parser.add_argument('name', help='name')
    add_parser.add_argument('number', type=phonenumber, help='phonenumber')
    add_phonebook_arg(add_parser)
    add_parser.set_defaults(func=add)

    lookup_parser = subparsers.add_parser('lookup', help='look up a phone number')
    lookup_parser.add_argument('name', help='adsf')
    add_phonebook_arg(lookup_parser)
    lookup_parser.set_defaults(func=lookup)

    change_parser = subparsers.add_parser('change', help='look up a phone number')
    change_parser.add_argument('name', help='name')
    change_parser.add_argument('number', type=phonenumber, help='phonenumber')
    add_phonebook_arg(change_parser)
    change_parser.set_defaults(func=change)

    reverselookup_parser = subparsers.add_parser('reverselookup', help='look up a phone number')
    reverselookup_parser.add_argument('name', help='adsf')
    add_phonebook_arg(reverselookup_parser)
    reverselookup_parser.set_defaults(func=reverselookup)

    return parser.parse_args(args)

if __name__ == '__main__':
    args = parse_args(sys.argv)
    print repr(args)
    print args
    args.func(**vars(args))
