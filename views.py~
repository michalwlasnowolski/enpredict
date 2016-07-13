# -*- coding: utf-8 -*-

from scripts.seq_cutter import SeqCutter
from scripts.kmers import Kmers
from scripts.spoil import Mutation
from django.http import JsonResponse
import json
from .models import WigFile
import pickle
from scripts.choose_classifier import Classifier
from django.shortcuts import render
from bokeh.plotting import figure
from bokeh.embed import components
from scripts.comparator import Comparator
from scripts.template_mutation import TemplateMutation
from StringIO import StringIO
from zipfile import ZipFile
from django.http import HttpResponse



def index(request):

    return render(request, 'enpredict/index.html')

def tutorial(request):

    return render(request, 'enpredict/tutorial.html', locals())

def compute_prediction(request):

       
    return render(request, 'enpredict/compute_prediction.html')

def mutate(request):

       
    return render(request, 'enpredict/mutate.html')

def resources_vista(request):

    database_name='Human VISTA (hg19)'

    records_list=[]
    for i in xrange(1, 23):
    
        chr_name='chr%i' % i
        record=WigFile.objects.filter(database='vista', chr_name=chr_name)
        records_list.append(record)

    return render(request, 'enpredict/resources.html', locals())

def resources_fly(request):
    chr_names=['chr2L', 'chr2R', 'chr3L', 'chr3R', 'chr4', 'chrX']

    records_list=[]
    database_name='Drosophila melanogaster (dm3)'


    for i in xrange(len(chr_names)):

        chr_name=chr_names[i]
        record=WigFile.objects.filter(database='fly', chr_name=chr_name)

        records_list.append(record)

    return render(request, 'enpredict/resources.html', locals())


def download_wigfile(request):     
   
    #list_of_files=request.POST.getlist('check_download')

    in_memory = StringIO()
    zip = ZipFile(in_memory, "a")
    list_of_files=['static/enpredict/data/vista.tar.gz']
    print 'hejo'
    for i in xrange(len(list_of_files)):

        file_path=list_of_files[i]
        filename=file_path.split('/')[-1]
        zip.write('/home/enpredict/lemonade/'+file_path, filename)
   
    # fix for Linux zip files read in Windows
    for file in zip.filelist:
        file.create_system = 0    
        
    zip.close()

    response = HttpResponse(content_type="application/zip")
    response["Content-Disposition"] = "attachment; filename=wigfiles.zip"
    
    in_memory.seek(0)    
    response.write(in_memory.read())
    
    return response







def compute(request):
    
    if request.method == 'POST':

        
        cutter=SeqCutter()
        sequence=cutter.make_string(request.POST[u'seq'].upper())
        count_kmers=Kmers()
        which_classifier=Classifier()        
        mutation=Mutation()
        list_database=request.POST.getlist('select_box[]')

        list_predictions=[]
        dict_color={'fantom_both':'#E1974C', 'fantom_brain':'#AB6857', 'fantom_heart':'#9067A7', 'vista_heart':'#D35E60', 'vista_neural':'#CCC210','vista_positives':'#7293CB', 'fly':'#84BA5B'}

        keys,dic=count_kmers.rc_kmers(count_kmers.all_kmers(4))

        for i in xrange(len(list_database)):
            
            print list_database[i]

            frame=0
            step=0
            
            if 'fly' in list_database[i]: frame=200; step=100
            elif 'fantom' in list_database[i]: frame=300; step=150
            elif 'vista' in list_database[i]: frame=1500; step=750
            
            color=dict_color[list_database[i]]
            which_classifier_name=which_classifier.choose_classifier(list_database[i])
            cut_seq=[sequence[(k*step):(k*step)+frame] for k in xrange(len(sequence)/step)]
            classifier = pickle.load(open(which_classifier_name))
            predictions=[mutation.prediction(count_kmers, seq, classifier, list_database[i], dic, keys, frame) for seq in cut_seq]
            prediction_range=[(l*step)+step for l in xrange(len(predictions))]
            list_predictions.append([prediction_range, predictions, color])
            
            

        plot=figure(title="Plot of enhancer prediction")
        plot.xaxis.axis_label = 'position'
        plot.yaxis.axis_label = 'probability of being an enhancer'
        
        x_parameters=[i[0] for i in list_predictions]
        y_parameters=[i[1] for i in list_predictions]
        
        colors=[i[2] for i in list_predictions]
        
        plot.multi_line(xs=x_parameters, ys=y_parameters, color=colors)
        
        script, div = components(plot)
        data={"the_script":script, "the_div":div}

        data_blank={}
        json_data= JsonResponse(data)
        return json_data
        


def spoil(request):
    
    if request.method == 'POST':

        count_kmers=Kmers()
        mutation=Mutation()
        comparator=Comparator()
        template_mutation=TemplateMutation()
        which_classifier=Classifier()   
        region=[]
        if len(request.POST[u'region'])!=0: 
            region=request.POST[u'region'].split(':')
            region=[int(x) for x in region]
        
        sequence=request.POST[u'seq'].upper()

        cut_off=float(request.POST[u'cut_off'])
        k_choice=int(request.POST[u'k_choice'])
        random_from_best=int(request.POST[u'random_from_best'])
        how_many_results=int(request.POST[u'num_outputs'])


        if 'fly' in request.POST[u'select']: frame=200
        elif 'fantom' in request.POST[u'select']: frame=300
        elif 'vista' in request.POST[u'select']: frame=1500
        else:
            print 'Error: wrong window length'
        if len(sequence)==frame:

            
            which_classifier_name=which_classifier.choose_classifier(request.POST[u'select'])
            classifier = pickle.load(open(which_classifier_name))
            results_pred_seq, reference_pred_seq=mutation.run_mutate(count_kmers, classifier, sequence, frame, k_choice, random_from_best, cut_off, how_many_results, region)
            list_seq_pred_pos=comparator.compare(reference_pred_seq, results_pred_seq)

        else:   
            print 'Error: wrong sequence lenght'

        
        original_prediction_list=[]
        new_prediction_list=[]
        all_data_string_list=[]
        all_positions_nucleo_string_box_list=[]
        seq_new_list=[]

        all_data=[]

        for i in xrange(len(list_seq_pred_pos)):

            original_prediction, new_prediction, all_data_string, all_positions_nucleo_string_box, seq_new=template_mutation.template_mutation(list_seq_pred_pos[i], reference_pred_seq)
            all_data.append([original_prediction, new_prediction, all_data_string, all_positions_nucleo_string_box, seq_new])
            original_prediction_list.append(original_prediction)
            new_prediction_list.append(new_prediction)
            all_data_string_list.append(all_data_string)
            all_positions_nucleo_string_box_list.append(all_positions_nucleo_string_box)
            seq_new_list.append(seq_new)

        data={'o_pred':original_prediction_list, 'n_pred':new_prediction_list, 'best_s':all_data_string_list, 'mutations':all_positions_nucleo_string_box_list, 'best_fasta_s':seq_new_list}
        json_data= JsonResponse(data)

        return json_data

