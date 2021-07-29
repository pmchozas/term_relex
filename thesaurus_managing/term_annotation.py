import os
import json
import csv
import nltk 
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import WordNetLemmatizer 
from nltk.stem import SnowballStemmer
#import spacy
#from spacy_spanish_lemmatizer import SpacyCustomLemmatizer

'''
filep=open('../data/listTerms_plurales.csv', 'w')
file_plu = csv.writer(filep)
new=open('../data/terms_json.csv', 'w')
file_terms = csv.writer(new)
newtxt=open('../data/synonyms.txt', 'w')
def read_terms(file):
	
	valuelist=[]
	lang_list=[]
	list_file=[]
	with open(file) as f:
		file = json.load(f)
	item=file[0]['@graph']
	for i in range(len(item)):
		list_file.append([])
		ide=item[i]['@id']
		item2=item[i]
		
		if('http://www.w3.org/2004/02/skos/core#prefLabel' in item2.keys()):
			w3pref=item2['http://www.w3.org/2004/02/skos/core#prefLabel']
			
			for j in range(len(w3pref)):
				value=w3pref[j]['@value']
				language=w3pref[j]['@language']
				if(language=='es'):
					valuelist.append(value.lower())
					#print('pref', value)
					list_file[i].append(value)
		if('http://www.w3.org/2004/02/skos/core#altLabel' in item2.keys() ):
			w3alt=item2['http://www.w3.org/2004/02/skos/core#altLabel']
			for j in range(len(w3alt)):
				value=w3alt[j]['@value']
				language=w3alt[j]['@language']
				if(language=='es'):
					valuelist.append(value.lower())
					#print('alt', value)
					list_file[i].append(value)
		
		
	
	for i in list_file:
		join=', '.join(i)
		print(i)
		if(len(i)>1):
			newtxt.write('"'+join+'"\n')

	valuelist_all=[]
	valuelist_largos=[]
	valuelist_cortos=[]
	for i in valuelist:
		file_terms.writerow([i])
		spl=i.split(' ')
		if(len(spl)>1):
			valuelist_largos.append(i)
			valuelist_all.append(i)
		else:
			valuelist_cortos.append(i)
	
	return(valuelist, valuelist_largos, valuelist_cortos, valuelist_all)

def plural_singular_uno(valuelist):
	porter = PorterStemmer()
	lancaster=LancasterStemmer()
	#lemmatizer = WordNetLemmatizer()
	#nlp = spacy.load("es")
	#lemmatizer = SpacyCustomLemmatizer()
	es_stemmer = SnowballStemmer('spanish')
	singular=[]
	plural=[]
	steam=[]
	
	for i in valuelist[2]:
		st=es_stemmer.stem(i)
		steam.append(st)
		if('es' not in i[-2:] or 's' not in i[-1:] ):
			#print(i)
			singular.append(i)
			valuelist[3].append(i)
			if('a' in i[-1:] or 'e' in i[-1:] or 'o' in i[-1:]):
				plu=i+'s'
				plural.append(plu.strip())
				file_plu.writerow([plu.strip()])
				valuelist[3].append(plu.strip())
				pass
			elif( 'l' in i[-1:] or 'y' in i[-1:] or 'd' in i[-1:] or 'r' in i[-1:]):
				plu=i+'es'
				#print(plu)
				plural.append(plu.strip())
				file_plu.writerow([plu.strip()])
				valuelist[3].append(plu.strip())
				pass
			elif('ón' in i[-2:] ):
				plu=' '+i[:-2]+'ones'
				#print(plu)
				plural.append(plu.strip())
				file_plu.writerow([plu.strip()])
				valuelist[3].append(plu.strip())
				pass
			elif('z' in i[-1:]):
				plu=i[:-1]+'ces'
				#print(plu)
				plural.append(plu.strip())
				file_plu.writerow([plu.strip()])
				valuelist[3].append(plu.strip())
				pass
		else:
			#print(i)
			plural.append(i.strip())
			file_plu.writerow([i])
			valuelist[3].append(i)
			if('es' in i[-2:]):
				sing=i[:-2]
				#print(sing)
				singular.append(sing)
				valuelist[3].append(sing)
				pass
			elif('s' in i[-1:] ):
				sing=i[:-1]
				singular.append(sing)
				valuelist[3].append(sing)
				pass
			elif('ces' in i[-1:]):
				sing=i[:-3]+'z'
				#print(sing)
				singular.append(sing)
				valuelist[3].append(sing)
				pass
				

	
	print(len(plural))
	print(len(singular))
	print(len(valuelist[3]))

	return(valuelist[3], steam, singular, plural)

def plural_singular_mas(valuelist):
	singular=[]
	plural=[]
	#print(len(valuelist[0]),len(valuelist[1]),len(valuelist[2]))
	for i in valuelist[1]:
		slp=i.split(' ')
		plu=''
		sing=''
		for j in slp:
			if('es' in j[-2:] or 's'  in j[-1:]):
				plu+=' '+j

			else:
				sing=i
				if(('a' in j[-1:]) or ('e' in j[-1:] ) or ('o' in j[-1:] )):
					if('de' == j or 'no' == j):
						plu+=' '+j
					else:
						plu+=' '+j+'s'
					
				elif( ('l' in j[-1:] ) or ('y' in j[-1:] ) or ('d' in j[-1:]) or ('r' in j[-1:] )):
					if('del' == j or 'y'==j or 'por'== j or 'salud' == j):
						plu+=' '+j
					else:
						plu+=' '+j+'es'
					
				elif('ón' in j[-2:]):
					plu+=' '+j[:-2]+'ones'
						
				elif('z' in j[-1:]):
					plu+=' '+j[:-1]+'ces'
					
				else:
					plu+=' '+j
		#print(i,'-',plu)
		plural.append(plu.strip())
		file_plu.writerow([plu.strip()])
		singular.append(sing)
	#print(plural)
	print(len(plural))
	print(len(singular))
	print(len(valuelist[3]))

	return(valuelist[1],plural)


def labelled_txt(list0, list1, list2, list3):
	file=open('../data/estatuto_es.txt', 'r', encoding='utf-8')
	read=file.readlines()
	new=open('../data/estatuto_es_span.txt', 'w')
	newc=open('../data/listTerms_conts.csv', 'w')
	conts = csv.writer(newc)
	
	
	ready=[]
	
	
	for i in read:
		cont=0
		for j in list1:
			low=i.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				find2=i[find:tam]
				find3='<span>'+find2+'</span>'
				i=i.replace(find2, find3)
		for j in list2:
			low=i.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				find2=i[find:tam]
				find3=' <span>'+find2+'</span> '
				i=i.replace(' '+find2+' ', find3)
		for j in list0:
			low=i.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				find2=i[find:tam]
				find3=' <span>'+find2+'</span> '
				i=i.replace(' '+find2+' ', find3)
		for j in list3:
			low=i.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				find2=i[find:tam]
				find3=' <span>'+find2+'</span> '
				i=i.replace(' '+find2+' ', find3)
			
			
		new.write(i)

	new.close()


def labelled_csv(list0, list1, list2, list3, list4, list5):
	#print(list0)
	file=open('2stset.csv', 'r', encoding='utf-8')
	#read=csv.reader(file)
	read=file.readlines()
	new=open('2stset_span.csv', 'w')
	qa = csv.writer(new)
	newc=open('listTerms_conts.csv', 'w')
	conts = csv.writer(newc)

	
	for i in range(len(read)):
		fila=read[i].replace('-','')
		cont=0
		for j in list1:
			low=fila.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				find2=fila[find:tam]
				find4=low[find:tam]
				caracter0=fila[find-1]
				caracter=fila[tam]
				print(caracter0,'|', find2, '|',caracter)
				find3=' <span>'+find2+'</span> '
				fila=fila.replace(' '+find2+' ', find3)
				fila=fila.replace(' '+find4+' ', find3)
				if(caracter==',' or caracter=='?' or caracter=='.'  or caracter==')'  or caracter==':'):
					fila=fila.replace(' '+find2+caracter, find3)

		for j in list2:
			low=fila.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				find2=fila[find:tam]
				find4=low[find:tam]
				caracter0=fila[find-1]
				caracter=fila[tam]
				print(caracter0,'|', find2, '|',caracter)
				find3=' <span>'+find2+'</span> '
				fila=fila.replace(' '+find2+' ', find3)
				fila=fila.replace(' '+find4+' ', find3)
				if(caracter==',' or caracter=='?' or caracter=='.'  or caracter==')'  or caracter==':'):
					fila=fila.replace(' '+find2+caracter, find3)
		for j in list4:
			low=fila.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				tam2=tam+1
				find2=fila[find:tam]
				find4=low[find:tam]
				caracter0=fila[find-1]
				caracter=fila[tam]
				print(caracter0,'|', find2, '|',caracter)
				find3=' <span>'+find2+'</span> '
				fila=fila.replace(' '+find2+' ', find3)
				fila=fila.replace(' '+find4+' ', find3)
				if(caracter==',' or caracter=='?' or caracter=='.'  or caracter==')'  or caracter==':'):
					fila=fila.replace(' '+find2+caracter, find3)
		for j in list5:
			low=fila.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				tam2=tam+1
				find2=fila[find:tam]
				find4=low[find:tam]
				caracter0=fila[find-1]
				caracter=fila[tam]
				print(caracter0,'|', find2, '|',caracter)
				find3=' <span>'+find2+'</span> '
				fila=fila.replace(' '+find2+' ', find3)
				fila=fila.replace(' '+find4+' ', find3)
				if(caracter==',' or caracter=='?' or caracter=='.'  or caracter==')'  or caracter==':'):
					fila=fila.replace(' '+find2+caracter, find3)
				
		for j in list3:
			low=fila.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				find2=fila[find:tam]
				find4=low[find:tam]
				caracter0=fila[find-1]
				caracter=fila[tam]
				print(caracter0,'|', find2, '|',caracter)
				find3=' <span>'+find2+'</span> '
				fila=fila.replace(' '+find2+' ', find3)
				fila=fila.replace(' '+find4+' ', find3)
				if(caracter==',' or caracter=='?' or caracter=='.'  or caracter==')'  or caracter==':'):
					fila=fila.replace(' '+find2+caracter, find3)
			
		#print(i)	
		spl=fila.split('?')
		pregunta=''
		respuesta=''
		if('?' not in fila and '"' not in fila[:1]):
			respuesta=fila
		elif(len(spl)>2):
			pregunta='?'.join(spl[:-1])
			pregunta=pregunta+'?'
			respuesta=spl[-1]
			respuesta=respuesta[2:]
		elif(len(spl)==2):
			pregunta=''.join(spl[:-1])
			pregunta=pregunta+'?'
			respuesta=spl[-1]
			respuesta=respuesta[2:]
		

		
		if(len(respuesta)>1):
			qa.writerow([pregunta, respuesta])
	
	new.close()


def cont(valuelist):
	file=open('input_article2_el.txt', 'r', encoding='utf-8')
	read=file.readlines()
	newc=open('listTerms_conts.csv', 'w')
	conts = csv.writer(newc)
	termino=''
	for i in valuelist[4]:
		#print(i)
		cont=0
		for j in read:
			if(' '+i+' ' in j.lower()):
				cont=cont+1
				termino=i

		#print(termino, cont)
		if(cont>0):
			conts.writerow([termino, cont])

'''

# Above Karen annotates with tuples. Below Patricia modifies the script to use lists


filep=open('../data/listTerms_plurales.csv', 'w')
file_plu = csv.writer(filep)
new=open('../data/terms_json.csv', 'w')
file_terms = csv.writer(new)
newtxt=open('../data/synonyms.txt', 'w')
def read_terms(file):
	
	valuelist=[]
	lang_list=[]
	list_file=[]
	with open(file) as f:
		file = json.load(f)
	item=file[0]['@graph']
	for i in range(len(item)):
		list_file.append([])
		ide=item[i]['@id']
		item2=item[i]
		
		if('http://www.w3.org/2004/02/skos/core#prefLabel' in item2.keys()):
			w3pref=item2['http://www.w3.org/2004/02/skos/core#prefLabel']
			
			for j in range(len(w3pref)):
				value=w3pref[j]['@value']
				language=w3pref[j]['@language']
				if(language=='es'):
					valuelist.append(value.lower())
					#print('pref', value)
					list_file[i].append(value)
		if('http://www.w3.org/2004/02/skos/core#altLabel' in item2.keys() ):
			w3alt=item2['http://www.w3.org/2004/02/skos/core#altLabel']
			for j in range(len(w3alt)):
				value=w3alt[j]['@value']
				language=w3alt[j]['@language']
				if(language=='es'):
					valuelist.append(value.lower())
					#print('alt', value)
					list_file[i].append(value)
		
		
	
	for i in list_file:
		join=', '.join(i)
		print(i)
		if(len(i)>1):
			newtxt.write('"'+join+'"\n')

	valuelist_all=[]
	valuelist_largos=[]
	valuelist_cortos=[]
	for i in valuelist:
		file_terms.writerow([i])
		spl=i.split(' ')
		if(len(spl)>1):
			valuelist_largos.append(i)
			valuelist_all.append(i)
		else:
			valuelist_cortos.append(i)
	
	return(valuelist, valuelist_largos, valuelist_cortos, valuelist_all)

def plural_singular_uno(valuelist):
	porter = PorterStemmer()
	lancaster=LancasterStemmer()
	#lemmatizer = WordNetLemmatizer()
	#nlp = spacy.load("es")
	#lemmatizer = SpacyCustomLemmatizer()
	es_stemmer = SnowballStemmer('spanish')
	singular=[]
	plural=[]
	steam=[]
	
	for i in valuelist:
		st=es_stemmer.stem(i)
		steam.append(st)
		if('es' not in i[-2:] or 's' not in i[-1:] ):
			#print(i)
			singular.append(i)
			valuelist.append(i)
			if('a' in i[-1:] or 'e' in i[-1:] or 'o' in i[-1:]):
				plu=i+'s'
				plural.append(plu.strip())
				file_plu.writerow([plu.strip()])
				valuelist.append(plu.strip())
				pass
			elif( 'l' in i[-1:] or 'y' in i[-1:] or 'd' in i[-1:] or 'r' in i[-1:]):
				plu=i+'es'
				#print(plu)
				plural.append(plu.strip())
				file_plu.writerow([plu.strip()])
				valuelist.append(plu.strip())
				pass
			elif('ón' in i[-2:] ):
				plu=' '+i[:-2]+'ones'
				#print(plu)
				plural.append(plu.strip())
				file_plu.writerow([plu.strip()])
				valuelist.append(plu.strip())
				pass
			elif('z' in i[-1:]):
				plu=i[:-1]+'ces'
				#print(plu)
				plural.append(plu.strip())
				file_plu.writerow([plu.strip()])
				valuelist.append(plu.strip())
				pass
		else:
			#print(i)
			plural.append(i.strip())
			file_plu.writerow([i])
			valuelist.append(i)
			if('es' in i[-2:]):
				sing=i[:-2]
				#print(sing)
				singular.append(sing)
				valuelist.append(sing)
				pass
			elif('s' in i[-1:] ):
				sing=i[:-1]
				singular.append(sing)
				valuelist.append(sing)
				pass
			elif('ces' in i[-1:]):
				sing=i[:-3]+'z'
				#print(sing)
				singular.append(sing)
				valuelist.append(sing)
				pass
				

	
# 	print(len(plural))
# 	print(len(singular))
# 	print(len(valuelist[3]))

	return(valuelist, steam, singular, plural)

def plural_singular_mas(valuelist):
	singular=[]
	plural=[]
	#print(len(valuelist[0]),len(valuelist[1]),len(valuelist[2]))
	for i in valuelist:
		slp=i.split(' ')
		plu=''
		sing=''
		for j in slp:
			if('es' in j[-2:] or 's'  in j[-1:]):
				plu+=' '+j

			else:
				sing=i
				if(('a' in j[-1:]) or ('e' in j[-1:] ) or ('o' in j[-1:] )):
					if('de' == j or 'no' == j):
						plu+=' '+j
					else:
						plu+=' '+j+'s'
					
				elif( ('l' in j[-1:] ) or ('y' in j[-1:] ) or ('d' in j[-1:]) or ('r' in j[-1:] )):
					if('del' == j or 'y'==j or 'por'== j or 'salud' == j):
						plu+=' '+j
					else:
						plu+=' '+j+'es'
					
				elif('ón' in j[-2:]):
					plu+=' '+j[:-2]+'ones'
						
				elif('z' in j[-1:]):
					plu+=' '+j[:-1]+'ces'
					
				else:
					plu+=' '+j
		#print(i,'-',plu)
		plural.append(plu.strip())
		file_plu.writerow([plu.strip()])
		singular.append(sing)
	#print(plural)
# 	print(len(plural))
# 	print(len(singular))
# 	print(len(valuelist[3]))

	return(valuelist,plural)


def labelled_txt(list0, list1, list2, list3):
	file=open('../data/estatuto_es.txt', 'r', encoding='utf-8')
	read=file.readlines()
	new=open('../data/estatuto_es_span.txt', 'w')
	newc=open('../data/listTerms_conts.csv', 'w')
	conts = csv.writer(newc)
	
	
	ready=[]
	
	
	for i in read:
		cont=0
		for j in list1:
			low=i.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				find2=i[find:tam]
				find3='<span>'+find2+'</span>'
				i=i.replace(find2, find3)
		for j in list2:
			low=i.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				find2=i[find:tam]
				find3=' <span>'+find2+'</span> '
				i=i.replace(' '+find2+' ', find3)
		for j in list0:
			low=i.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				find2=i[find:tam]
				find3=' <span>'+find2+'</span> '
				i=i.replace(' '+find2+' ', find3)
		for j in list3:
			low=i.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				find2=i[find:tam]
				find3=' <span>'+find2+'</span> '
				i=i.replace(' '+find2+' ', find3)
			
			
		new.write(i)

	new.close()


def labelled_csv(list0, list1, list2, list3, list4, list5):
	#print(list0)
	file=open('2stset.csv', 'r', encoding='utf-8')
	#read=csv.reader(file)
	read=file.readlines()
	new=open('2stset_span.csv', 'w')
	qa = csv.writer(new)
	newc=open('listTerms_conts.csv', 'w')
	conts = csv.writer(newc)

	
	for i in range(len(read)):
		fila=read[i].replace('-','')
		cont=0
		for j in list1:
			low=fila.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				find2=fila[find:tam]
				find4=low[find:tam]
				caracter0=fila[find-1]
				caracter=fila[tam]
				print(caracter0,'|', find2, '|',caracter)
				find3=' <span>'+find2+'</span> '
				fila=fila.replace(' '+find2+' ', find3)
				fila=fila.replace(' '+find4+' ', find3)
				if(caracter==',' or caracter=='?' or caracter=='.'  or caracter==')'  or caracter==':'):
					fila=fila.replace(' '+find2+caracter, find3)

		for j in list2:
			low=fila.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				find2=fila[find:tam]
				find4=low[find:tam]
				caracter0=fila[find-1]
				caracter=fila[tam]
				print(caracter0,'|', find2, '|',caracter)
				find3=' <span>'+find2+'</span> '
				fila=fila.replace(' '+find2+' ', find3)
				fila=fila.replace(' '+find4+' ', find3)
				if(caracter==',' or caracter=='?' or caracter=='.'  or caracter==')'  or caracter==':'):
					fila=fila.replace(' '+find2+caracter, find3)
		for j in list4:
			low=fila.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				tam2=tam+1
				find2=fila[find:tam]
				find4=low[find:tam]
				caracter0=fila[find-1]
				caracter=fila[tam]
				print(caracter0,'|', find2, '|',caracter)
				find3=' <span>'+find2+'</span> '
				fila=fila.replace(' '+find2+' ', find3)
				fila=fila.replace(' '+find4+' ', find3)
				if(caracter==',' or caracter=='?' or caracter=='.'  or caracter==')'  or caracter==':'):
					fila=fila.replace(' '+find2+caracter, find3)
		for j in list5:
			low=fila.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				tam2=tam+1
				find2=fila[find:tam]
				find4=low[find:tam]
				caracter0=fila[find-1]
				caracter=fila[tam]
				print(caracter0,'|', find2, '|',caracter)
				find3=' <span>'+find2+'</span> '
				fila=fila.replace(' '+find2+' ', find3)
				fila=fila.replace(' '+find4+' ', find3)
				if(caracter==',' or caracter=='?' or caracter=='.'  or caracter==')'  or caracter==':'):
					fila=fila.replace(' '+find2+caracter, find3)
				
		for j in list3:
			low=fila.lower()
			find=low.find(j)
			if(find>0):
				tam=len(j)+find
				find2=fila[find:tam]
				find4=low[find:tam]
				caracter0=fila[find-1]
				caracter=fila[tam]
				print(caracter0,'|', find2, '|',caracter)
				find3=' <span>'+find2+'</span> '
				fila=fila.replace(' '+find2+' ', find3)
				fila=fila.replace(' '+find4+' ', find3)
				if(caracter==',' or caracter=='?' or caracter=='.'  or caracter==')'  or caracter==':'):
					fila=fila.replace(' '+find2+caracter, find3)
			
		#print(i)	
		spl=fila.split('?')
		pregunta=''
		respuesta=''
		if('?' not in fila and '"' not in fila[:1]):
			respuesta=fila
		elif(len(spl)>2):
			pregunta='?'.join(spl[:-1])
			pregunta=pregunta+'?'
			respuesta=spl[-1]
			respuesta=respuesta[2:]
		elif(len(spl)==2):
			pregunta=''.join(spl[:-1])
			pregunta=pregunta+'?'
			respuesta=spl[-1]
			respuesta=respuesta[2:]
		

		
		if(len(respuesta)>1):
			qa.writerow([pregunta, respuesta])
	
	new.close()


def cont(valuelist):
	file=open('input_article2_el.txt', 'r', encoding='utf-8')
	read=file.readlines()
	newc=open('listTerms_conts.csv', 'w')
	conts = csv.writer(newc)
	termino=''
	for i in valuelist:
		#print(i)
		cont=0
		for j in read:
			if(' '+i+' ' in j.lower()):
				cont=cont+1
				termino=i

		#print(termino, cont)
		if(cont>0):
			conts.writerow([termino, cont])




#MAIN


# file='../data/labourlaw_thesaurus.json'
# uno=read_terms(file)
# print('ESTO ES UNO')
# print(uno)

file=open('../data/filtered_terms.txt', 'r')
uno=[]
for t in file.readlines():
    uno.append(t.strip('\n'))

print(uno)

dos=plural_singular_uno(uno)
plural_singular_cortos_list=dos[0]
singular_cortos_list=dos[2]
plural_cortos_list=dos[3]
stemmer=dos[1]
mas=plural_singular_mas(uno)
singular_largos_list=mas[0]
plural_largos_list=mas[1]
labelled_txt(plural_singular_cortos_list, singular_largos_list, plural_largos_list, stemmer)
#labelled_csv(plural_singular_cortos_list, singular_largos_list, plural_largos_list, stemmer,plural_cortos_list,singular_cortos_list )
