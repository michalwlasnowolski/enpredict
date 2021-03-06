# adding html tags to results of 'mutate' tool
class TemplateMutation():

    def template_mutation(self, result_pred_seq, reference_pred_seq):

        seq_new=result_pred_seq[1]

        len_best_sequence=len(result_pred_seq[1])
        original_prediction=str(reference_pred_seq[0])
        new_prediction=str(result_pred_seq[0])

        positions_mutation=[]

        all_positions_nucleo=result_pred_seq[2]


        for i in xrange(len(all_positions_nucleo)):
            positions_mutation.append(all_positions_nucleo[i][0])

        nums=range(10,len_best_sequence+10,10)

        line_with_nums=[]
        for i in nums:
            line=[str(i)]
            while len("".join(line))!=11: 
                line.insert(0, ' ')
            if (i%50)==0: line.append('<br>')  

            line_str="".join(line)
            line_with_nums.append(line_str)
        line_with_nums.append('<br>')


        all_lines_seq=[]
        one_line_seq=[]
        for i in xrange(0,len_best_sequence,10):

            line_seq=[seq_new[i:i+10]]

            if ((i+10)%50)==0 and i!=0:
                line_seq.append('<br>')
                
                line_seq_space="".join(line_seq)
                all_lines_seq.append(line_seq_space)
                one_line_seq=[]
            else: 
                line_seq.append(' ')
                line_seq_space="".join(line_seq)
                all_lines_seq.append(line_seq_space)

        all_data=[]
        for i in xrange(0, len(line_with_nums), 5):
            all_data.append("".join(line_with_nums[i:i+5]))
            
            all_data.append("".join(all_lines_seq[i:i+5]))

        for i in positions_mutation:
            pos=-1

            for j in xrange(len(all_data)):
                for k in xrange(len(all_data[j])):
                    if all_data[j][k]=='A' or all_data[j][k]=='C' or all_data[j][k]=='G' or all_data[j][k]=='T':
                        pos+=1
                        if i==pos: 
                            string='<span style="color: red">%s</span>' % all_data[j][k]
                            line_before_nuc=all_data[j][:k]
                            line_after_nuc=all_data[j][k+1:]
                            whole_line=line_before_nuc+string+line_after_nuc
                            all_data[j]=whole_line
                            
        all_data_string="".join(all_data)

        all_positions_nucleo_string=[]
        for i in xrange(len(all_positions_nucleo)):
            line='%i) %s -> %s on positions [%s]' % (i+1, all_positions_nucleo[i][1], all_positions_nucleo[i][2], int(all_positions_nucleo[i][0])+1)
            all_positions_nucleo_string.append(line)

        all_positions_nucleo_string_box=''
        for i in xrange(len(all_positions_nucleo_string)):
            all_positions_nucleo_string_box+=all_positions_nucleo_string[i]
            all_positions_nucleo_string_box+='<br>'


        return original_prediction, new_prediction, all_data_string, all_positions_nucleo_string_box, seq_new

