import sys
from Bio import Seq
from collections import Counter

class Kmers():


    def all_kmers(self, k=4):
        s=[""]
        for i in xrange(k):
            s2=[]
            for i in s:
                for a in "ACGT":
                    s2.append(i+a)
            s=s2
        return s


    def rc_kmers(self, kmers):
        res={}
        keys=[]
        for s in kmers:
            if Seq.reverse_complement(s) in keys:
                res[s]=Seq.reverse_complement(s)
            else:
                keys.append(s)
                res[s]=s
        return keys,res


    def count_vec(self, s, dic, keys, seq_len):

         d=Counter([dic[s[i:i+4]] for i in range(len(s)-3)])

         return [float(d[k])/seq_len for k in keys]





