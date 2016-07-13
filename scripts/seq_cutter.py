import sys

class SeqCutter():

    def make_string(self, fasta):

            sequence=''
            for i in xrange(len(fasta)):
                    seq=fasta[i].strip()
                    sequence+=seq
            return sequence

