import os


class FilesListMaker():

    def make_fileslist(self):

        list_files=open('/home/enpredict/lemonade/static/enpredict/files_list/files_list.txt', 'w')
        if_first_line=True
        for root, dirs, files in os.walk("/home/enpredict/lemonade/static/enpredict/data/", topdown=False):
            for name in files:


		        name=os.path.join(root, name)

		        if name[-3:]=='wig':
			
			        for i in xrange(len(name)):
				        if name[-i-1] == '/':

					        if if_first_line==True:
						        if_first_line=False
					        else:
						        list_files.write('\n')
					        list_files.write(name[-i:])
					        break
					
        list_files.close()

