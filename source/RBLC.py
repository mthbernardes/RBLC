import os
import sys
import fnmatch
from datetime import datetime

def list_dirs():
	folder_log = sys.argv[1]
	for root, dir, files in os.walk(folder_log):
		print root
		print ""
		for file in fnmatch.filter(files, "*"):
				print "..." + file
				get_infos(root,file)
				print
		print ""
		
def get_infos(root,file):
	pathbase = root+'\\'+file
	try:
		file = open(pathbase,'r')
		for linha in file:
			linha = linha.strip()
			if 'Iniciado' in linha:
				data_inicio = datetime.strptime(linha.split(':',1)[1].strip(),'%a %b %d %H:%M:%S %Y').strftime("%d/%m/%y")
				print '...Data Inicio:\t',data_inicio
			if 'Finalizado em:' in linha:
				data_fim = datetime.strptime(linha.split(':',1)[1].strip(),'%a %b %d %H:%M:%S %Y').strftime("%d/%m/%y")
				print '...Data Fim:\t',data_fim
			if 'Arquivos:    ' in linha:
				erros = int(linha.split()[5])
				print '...Erros:\t',erros
				
		file.close()
	except Exception as e:
		print 'Erro ao ler o arquivo, motivo do erro: '+str(e)
		
if len(sys.argv) < 2:
	print 'Informa o caminho da pasta de logs'
	exit()
else:
	list_dirs()
