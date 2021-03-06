from django.core.management.base import BaseCommand
from enpredict.models import WigFile
from enpredict.scripts.files_list import FilesListMaker



class WigFileCreator():


    def find_path(self, database, modification, kmers, specific_tissue, file_name):

        path=''
        static_path='enpredict/data/'


        classificator=''


        if database=='fly':
        
            database='fly/'

            if modification == 'yes' and kmers=='yes':
                classificator = 'modification_4mers/'

            elif modification == 'yes' and kmers=='no':
                classificator = 'modification/'

            elif modification == 'nomodification' and kmers=='yes':
                classificator = '4mers/'

            path+=database+classificator+file_name
            static_path+=database+classificator+file_name

        else:

            adres='%s/%s_%s_%s/%s' % (database, database, specific_tissue, modification, file_name)

            path+=adres
            static_path+=adres
        return path, static_path



    def create_wigfile(self, file_info, file_name):


        species=''
        specific_tissue='no'
        modification='nomodification'
        kmers='no'

        chr_name=file_info[0]
        frame=file_info[1]
        step=file_info[2]
        database=''
        

        if 'vista' in file_info:
            database = 'vista'
        if 'fantom' in file_info:
            database = 'fantom'
        if 'fly' in file_info:
            database = 'fly'


        if database == 'vista' or database == 'fantom':
            species='Hs'
        else:
            species='Dm'

        if 'heart' in file_info:
            specific_tissue = 'heart'
        if 'heart2steps' in file_info:
            specific_tissue = 'heart2steps'
        if 'both' in file_info:
            specific_tissue = 'both'
        if 'positives' in file_info:
            specific_tissue = 'positives'
        if 'brain' in file_info:
            specific_tissue = 'brain'
        if 'brain2steps' in file_info:
            specific_tissue = 'brain2steps'

        if 'h1hesc' in file_info:
            modification='h1hesc'
        if 'tier1' in file_info:
            modification='tier1'
        if 'tier12' in file_info:
            modification='tier12'
        if 'modification' in file_info:
            modification='yes'
        if '4mers' in file_info:
            kmers = 'yes'



        file_path, file_static_path=self.find_path(database, modification, kmers, specific_tissue, file_name)

        wigfile = WigFile.objects.create(species=species, frame=frame, step=step, chr_name=chr_name, database=database, modification=modification, kmers=kmers, specific_tissue=specific_tissue, file_path=file_path, file_static_path=file_static_path)



        print 'WigFile created ' + chr_name,database, modification





class Command(BaseCommand):



    def handle(self, *args, **options):        




        WigFile.objects.all().delete()

        list_maker=FilesListMaker()
        list_maker.make_fileslist()

        path_to_file='/home/enpredict/lemonade/static/enpredict/files_list/files_list.txt'
        files_list=[]

        files_list=[x.strip() for x in open(path_to_file)]


        for i in xrange(len(files_list)):
            
            file_name=files_list[i]
            
            file_info = files_list[i][:-4].split('_')


            wigfile = WigFileCreator()
            wigfile.create_wigfile(file_info, file_name)




a=Command()
