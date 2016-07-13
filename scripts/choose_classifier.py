
class Classifier():



    def choose_classifier(self,classifier_name):

        classifiers=['fantom_both__4mers', 'fantom_brain__4mers', 'fantom_heart__4mers', 'fly_4mers_100', 'vista_heart__4mers', 'vista_neural__4mers', 'vista_positives__4mers']
        
        path='/home/enpredict/lemonade/static/enpredict/classifiers/'
        if classifier_name=='fantom_both':
            path+=classifiers[0]
        if classifier_name=='fantom_brain':
            path+=classifiers[1]
        if classifier_name=='fantom_heart':
            path+=classifiers[2]
        if classifier_name=='fly':
            path+=classifiers[3]
        if classifier_name=='vista_heart':
            path+=classifiers[4]
        if classifier_name=='vista_neural':
            path+=classifiers[5]
        if classifier_name=='vista_positives':
            path+=classifiers[6]
        
        return path

