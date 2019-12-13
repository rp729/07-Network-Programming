import optparse
import subprocess


class BadAssBull:
    def __init__(self,macchanger,ipspoof):
        self.macchanger = macchanger
        self.ipspoof = ipspoof

    def entry_page():
        file = open("bull.txt")
        print(file.read())
        input()

    def options(self):
        file = open("options.txt")
        print()

badass = BadAssBull
BadAssBull.entry_page()