import pickle
import random

class Mutation():

    # compute prediction of being enhancer
    def prediction(self, count_kmers, seq, classifier, which_database, dic, keys, frame):


        kmers=count_kmers.count_vec(seq, dic, keys, frame)

        predicted = classifier.predict_proba(kmers)
        list_predicted=[]
        predicted_len=len(predicted)
        for i in xrange(predicted_len):
            list_predicted.append(float(predicted[i][1]))

        return list_predicted[0]
        

    #create all possible sequences with point mutation
    def find_mutations(self, s, region):
        all=set(["A","C","G","T"])
        nucs=list(s)
        seqs=[]

        for i,nuc in enumerate(nucs):

            if len(region)==0: 

                for mut in all-set([nuc]):
                    yield ["".join(nucs[:i]+[mut]+nucs[i+1:]), '%i%s' % (i, mut)]
            else:
                if i>=(region[0]-1) and i<= (region[1]-1):
                              
                    for mut in all-set([nuc]):
                        yield ["".join(nucs[:i]+[mut]+nucs[i+1:]), '%i%s' % (i, mut)]



    def mutate(self, count_kmers, dic, keys, classifier, all_seq, candidates, results, how_many_best, how_many_random, cut_off, frame, region):


        candidate=candidates[0]

        del(candidates[0])

        seqs=[x for x in self.find_mutations(candidate[1], region)]
        for_kmers=[]
        mut_syms=[]

        if len(candidate[2])>1: old_muts=candidate[2].split('_')
        else: old_muts=[]
        
        for i in seqs:

            new_seq_mut="_".join(sorted(list([i[1]] + old_muts)))
            if not new_seq_mut in all_seq: 
                for_kmers.append(i[0])
                mut_syms.append(new_seq_mut)

                all_seq[new_seq_mut]=''

        if len(for_kmers)!=0:
            kmers=[count_kmers.count_vec(x, dic, keys, frame) for x in for_kmers]
            predicted = [classifier.predict_proba(i)[0][1] for i in kmers]
            seq_pred=sorted(zip(predicted, for_kmers, mut_syms))[:how_many_best]
            new_candidates=random.sample(seq_pred[1:], how_many_random)+[seq_pred[0]]


            list_results_seq=[i[1] for i in results]
        

            for i in new_candidates:
                if i[0]<= cut_off and i[1] not in list_results_seq:
                    results.append(i)
                else:
                    candidates=candidates+[i]

        return candidates, all_seq, results

    def run_mutate(self, count_kmers, classifier, sequence, frame, how_many_best, how_many_random, cut_off, how_many_results, region):


        all_seq={}


        keys,dic=count_kmers.rc_kmers(count_kmers.all_kmers(4))


        results=[]
        reference_pred_seq=[classifier.predict_proba(count_kmers.count_vec(sequence, dic, keys, frame))[0][1], sequence, '']
        candidates = [[classifier.predict_proba(count_kmers.count_vec(sequence, dic, keys, frame))[0][1], sequence, '']]
        z=0




        while len(candidates)!=0:
            z+=1

            candidates, all_seq, results=self.mutate(count_kmers, dic, keys, classifier, all_seq, candidates, results, how_many_best, how_many_random, cut_off, frame, region)

            print "there is %i candidates, %i results and %i iteration" % (len(candidates), len(results), z)

            if len(results)>=how_many_results:
                results=list(results[:how_many_results])

                break

        return results, reference_pred_seq
