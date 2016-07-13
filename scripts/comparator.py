class Comparator():

    # compare mutated sequence with the original 
    def compare(self, reference_pred_seq, list_results):

        reference_seq=reference_pred_seq[1]


        for i in xrange(len(list_results)):
            result_seq=list_results[i][1]
            mutations=[]

            for j in xrange(len(reference_seq)):
                
                if reference_seq[j] != result_seq[j]:

                    mutations.append([j, reference_seq[j], result_seq[j]])
            list_results[i]=list(list_results[i])
            list_results[i][-1]=mutations

        return list_results

