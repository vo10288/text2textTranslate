#!/usr/bin/python3

import time
from datetime import datetime
import argparse
import googletrans
from googletrans import Translator
from gtts import gTTS 
import subprocess
import os


print(("""\

_____________________________________
( SPEECH TRANSLATE IN PYTHON BY              )
( VISI@N                              )
-------------------------------------
	""").encode('utf-8'))
     
print(("""\
__     ___     _   ____        
\ \   / (_)___(_) / __ \ _ __  
 \ \ / /| / __| |/ / _` | '_ \ 
  \ V / | \__ \ | | (_| | | | |
   \_/  |_|___/_|\ \__,_|_| |_|
                  \____/       
	""").encode('utf-8'))
    
print(("""\
	"Afrikaans": "South Africa", "af-ZA",
	"Arabic" : "Algeria","ar-DZ","Bahrain","ar-BH","Egypt","ar-EG","Israel","ar-IL","Iraq","ar-IQ","Jordan","ar-JO","Kuwait","ar-KW",
				"Lebanon","ar-LB","Morocco","ar-MA","Oman","ar-OM","Palestinian Territory","ar-PS","Qatar","ar-QA","Saudi Arabia","ar-SA",
				"Tunisia","ar-TN","UAE","ar-AE",
	"Basque": "Spain", "eu-ES",
	"Bulgarian": "Bulgaria", "bg-BG",
	"Catalan": "Spain", "ca-ES",
	"Chinese Mandarin": "China (Simp.)", "cmn-Hans-CN","Hong Kong SAR (Trad.)", "cmn-Hans-HK","Taiwan (Trad.)", "cmn-Hant-TW",
	"Chinese Cantonese": "Hong Kong", "yue-Hant-HK",
	"Croatian": "Croatia", "hr_HR",
	"Czech": "Czech Republic", "cs-CZ",
	"Danish": "Denmark", "da-DK",
	"English": "Australia", "en-AU","Canada", "en-CA","India", "en-IN","Ireland", "en-IE","New Zealand", "en-NZ","Philippines", "en-PH",
				"South Africa", "en-ZA","United Kingdom", "en-GB","United States", "en-US",
	"Farsi": "Iran", "fa-IR",
	"French": "France", "fr-FR",
	"Filipino": "Philippines", "fil-PH",
	"Galician": "Spain", "gl-ES","German": "Germany", "de-DE",
	"Greek": "Greece", "el-GR",
	"Finnish": "Finland", "fi-FI",
	"Hebrew" :"Israel", "he-IL",
	"Hindi": "India", "hi-IN",
	"Hungarian": "Hungary", "hu-HU",
	"Indonesian": "Indonesia", "id-ID",
	"Icelandic": "Iceland", "is-IS",
	"Italian": "Italy", "it-IT","Switzerland", "it-CH",
	"Japanese": "Japan", "ja-JP",
	"Korean": "Korea", "ko-KR",
	"Lithuanian": "Lithuania", "lt-LT",
	"Malaysian": "Malaysia", "ms-MY",
	"Dutch": "Netherlands", "nl-NL","Norwegian": "Norway", "nb-NO",
	"Polish": "Poland", "pl-PL",
	"Portuguese": "Brazil", "pt-BR","Portugal", "pt-PT",
	"Romanian": "Romania", "ro-RO",
	"Russian": "Russia", "ru-RU","Serbian": "Serbia", "sr-RS","Slovak": "Slovakia", "sk-SK","Slovenian": "Slovenia", "sl-SI",
	"Spanish": "Argentina", "es-AR","Bolivia", "es-BO","Chile", "es-CL","Colombia", "es-CO","Costa Rica", "es-CR","Dominican Republic", 
				"es-DO","Ecuador", "es-EC","El Salvador", "es-SV","Guatemala", "es-GT","Honduras", "es-HN","Mexico", "es-MX",
				"Nicaragua", "es-NI","Panama", "es-PA","Paraguay", "es-PY","Peru", "es-PE","Puerto Rico", "es-PR","Spain", "es-ES",
				"Uruguay", "es-UY","United States", "es-US","Venezuela", "es-VE",
	"Swedish": "Sweden", "sv-SE",
	"Thai": "Thailand", "th-TH",
	"Turkish": "Turkey", "tr-TR",
	"Ukrainian": "Ukraine", "uk-UA",
	"Vietnamese": "Viet Nam", "vi-VN",
	"Zulu": "South Africa", "zu-ZA"

	""").encode('utf-8'))


translator = Translator()  


# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dir", default="inputText", required=True,
	help="directory of file input")
ap.add_argument("-i", "--input", default="en",#required=True,
	help="lang input")
ap.add_argument("-o", "--output", default="en",#required=True,
	help="lang output")
args = vars(ap.parse_args())

timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

TEXToutput = ('TEXT_'+str(args["input"])+str(args["output"])+'_'+str(timestamp))
MP3output = ('MP3_'+str(args["input"])+str(args["output"])+'_'+str(timestamp))
MP3ALLoutput = ('MP3ALL_'+str(args["input"])+str(args["output"])+'_'+str(timestamp))
    
if not os.path.exists(TEXToutput):
	os.makedirs(TEXToutput)

if not os.path.exists(MP3output):
	os.makedirs(MP3output)

if not os.path.exists(MP3ALLoutput):
	os.makedirs(MP3ALLoutput)

#d =  open(sys.argv[1])
d = os.listdir(str(args["dir"]))

####################################################################################
for files in d:
	print('file : '+(str(args["dir"]))+'/'+files)
	
	f = open((str(args["dir"]))+'/'+files)#,readlines()
	for riga in f:
		riga = str (riga)
		print('riga : '+riga)
		
		###########################
		
		if (riga == ">"):   #
			
			continue
		
		if (riga == "\n"):   #
			
			continue
		
		else:

		
		
			###########################
		
			rigatransN = translator.translate(riga, dest=(args["output"])).text
		
			time.sleep(2)
			documento = open(TEXToutput+'/'+timestamp+'_'+files, "a")
			documento.write(rigatransN)
			documento.write("\n")

			documento.close()
		
			time.sleep(2)
		
			comando = ('say '+'\"'+str(rigatransN)+'\"')
			subprocess.Popen(comando, shell=True)
		
			time.sleep(2)
				

			###########################
			
			timestamp2 = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

		
			# Language in which you want to convert 
			global language
			language = (args["output"])
			# have a high speed 
			myobj = gTTS(text=rigatransN, lang=language, slow=False) 
			# welcome  
			myobj.save(MP3output+'/'+timestamp2+'.mp3') 
			time.sleep(4)
			# Playing the converted file 
			os.system('mplayer '+MP3output+'/'+timestamp2+'.mp3"')
		
			time.sleep(4)
		
			comando = ('cat '+MP3output+'/'+timestamp2+'.mp3'+' >> '+MP3ALLoutput+'/'+timestamp+'_'+files+'.mp3')
			subprocess.Popen(comando, shell=True)
		
exit
