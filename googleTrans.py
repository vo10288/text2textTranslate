#!/usr/bin/python3

# by Antonio "Visi@n" Broi antonio@tsurugi-linux.org
# https://tsurugi-linux.org 
# 20210613

# 
# LICENSE M.I.T. https://opensource.org/licenses/MIT
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS 
#OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR 
#OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import sys
import os
import locale
import subprocess
import googletrans
from googletrans import Translator
import subprocess
import signal
import time
from datetime import datetime
import argparse

os.environ["PYTHONIOENCODING"] = "utf-8" 
myLocale=locale.setlocale(category=locale.LC_ALL, locale="en_GB.UTF-8") 


print(("""\

  _____________________________________
( TRANSLATE IN PYTHON BY              )
( VISION                              )
 -------------------------------------
    """).encode('utf-8'))
     
daemon=(("""\
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;l0Oo;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;:0WW0d:;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;:OMMMWk;;;;;;;;;;;;;;;;;;:lldolc:;;;;;;;
;;;;;;;;;;;;;;;;;;;;kMMMMM0;;;;;;;;;;;;;;;;;cOWMMMMWk;;;;;;;
;;;;;;;;;;;;;;;;;;;cXMMMMMk;;;;;;;;;;;;;;;;dXMNNMMMMO;;;;;;;
;;;;;;;;;;;;;;;;;;oKMMMMW0c;;;;;;;;;;;;;;;oNM0ckMMMWd;;;;;;;
;;;;;;;;;;;;;;;;;oNMMMMXo:;;;;;;;;;;;;;;;;OMMocOMMMO:;;;;;;;
;;;;;;;;;;;;;;;;lXMMMMXo:cllollll:;;;;;;;oXN0cxWMMMk;;;;;;;;
;;;;;;;;;;;;;;;dXMMMMMXKKNWWMMMMMKxo:;;;;kWx:;kMMMNx;;;;;;;;
;;;;;;;;;;;;;;oXMMMM0olldxk0KNMMMMMWKl;;c0O:;;kMMMO:;;;;;;;;
;;;;;;;;;;;;:oXMMMKd:;;;;;;;;dNMMMMMNd;cKMd;;:OMMMk:;;;;;;;;
;;;;;;;;;;:d0WMMM0c;:odOKKO0K0kkk0KOl;c0MNo;;oNMMNx:;;;;;;;;
;;;;;;;:okKWMMMNOkO0KMMMMMMMXo;;:d0K0k0MWk:;;dMMM0c:;;;;;;;;
;;;;dKKXWMMMMMKo:OMMMMMMMMMMKkxolx0NMMMMO:;;;dMMMO:;;;;;;;;;
;;;;:odOXXK0xxdx0N0kXMMMMMMMMMMMNl;kMMMKc;;;;dMMMk;;;;;;;;;;
;;;;;;;:c:;:xXWX00O0NMMMX0k0WMMMXl;kMMM0;;;;;dMMMk;;;;;;;;;;
;;;;;;;;;;;dMM0OKWMMWMMMN0OKWWX0l;lKMMM0;;;;;dMMMk;;;;;;;;;;
;;;;;;;;;;;lXMMMMMMN0MMMMMXOkl:;;;dNMMM0;;;;;dMMMk;;;;;;;;;;
;;;;;;;;;;;;xWMMMXONMMMMMMMWOc;;;;:kMMM0;;;;;dMMMk;;;;;;;;;;
;;;;;;;;;;;;:kWMMk;kWMMN00koc;;;::;cXMWk;;;;;oMMMk;;;;;;;;;;
;;;;;;;;;;;;;:lll:cOMMMO;;;;;;;dKo;;xWO:;;;;;dMMMk;;;;;;;;;;
;;;;;;;;;;;;;;;;;cKWMMNxlc;;;:dKXl;;:lc;;;;;;OMMMk;;;;;;;;;;
;;;;;;;;;;;;;cokOXMMMMWWWNXOk0MMO:;;;;cdllc:lKMMMk;;;;;;;;;;
;;;;;;;;;;;;oXMMMMMMXxodk0NMMMMMO:;;;;:0MWXXWMMMNd;;;;;;;;;;
;;;;;;;;;;;;kMMMMMMNd;;;;;oXMMMMNo;;;;;lKMMMMMMM0:;;;;;;;;;;
;;;;;;;;;;;c0MMMMWOl;;;;;;;cxNMW0c;;;;;;:kWMMMMMx;;;;;;;;;;;
;;;;;;;;;;;;kMMMNd;;;;;;;;;;;dKk:;;;;;;;;;0MMMWXl;;;;;;;;;;;
;;;;;;;;;;;;lOOdc;;;;;;;;;;;;;:;;;;;;;;;;;xNMXo:;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;lko;;;;;;;;;;;;;;

    """).encode('utf-8'))
    
print(("""\
'af':'afrikaans','sq':'albanian','am':'amharic','ar':'arabic','hy':'armenian','az':'azerbaijani',
'eu': 'basque','be':'belarusian','bn':'bengali','bs':'bosnian','bg':'bulgarian','ca':'catalan',
'ceb':'cebuano','ny':'chichewa','zh-cn':'chinese(simplified)','zh-tw':'chinese(traditional)',
'co':'corsican','hr':'croatian','cs':'czech','da':'danish','nl':'dutch','en':'english',
'eo':'esperanto','et':'estonian','tl':'filipino','fi':'finnish','fr':'french','fy':'frisian',
'gl':'galician','ka':'georgian','de':'german','el':'greek','gu': 'gujarati','ht':'haitian creole',
'ha':'hausa','haw':'hawaiian','iw':'hebrew','hi':'hindi','hmn':'hmong','hu':'hungarian',
'is':'icelandic','ig':'igbo','id':'indonesian','ga':'irish','it': 'italian','ja': 'japanese',
'jw':'javanese','kn':'kannada','kk':'kazakh','km':'khmer','ko':'korean','ku': 'kurdish (kurmanji)',
'ky':'kyrgyz','lo':'lao','la':'latin','lv':'latvian','lt':'lithuanian','lb':'luxembourgish',
'mk':'macedonian','mg':'malagasy','ms':'malay','ml':'malayalam','mt':'maltese','mi':'maori',
'mr':'marathi','mn':'mongolian',  'my':'myanmar (burmese)','ne':'nepali','no':'norwegian','ps':'pashto',
'fa':'persian','pl':'polish',     'pt':'portuguese','pa':'punjabi','ro':'romanian','ru': 'russian',
'sm':'samoan','gd':scots gaelic','sr':'serbian','st':'sesotho','sn':'shona','sd':'sindhi',
'si':'sinhala','sk':'slovak','sl':'slovenian','so':'somali','es':'spanish','su':'sundanese',    
'sw':swahili','sv':'swedish','tg':'tajik','ta':'tamil','te':'telugu','th': 'thai',
'tr':'turkish','uk':'ukrainian','ur':'urdu','uz':'uzbek','vi':'vietnamese','cy':'welsh',
'xh':'xhosa','yi':'yiddish','yo':'yoruba','zu':'zulu','fil':'Filipino','he':'Hebrew'
    
    """).encode('utf-8'))
    

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--daemon", default="d",
	help="you can change the first languange, default en")
ap.add_argument("-1", "--lang1", default="en",
	help="you can change the first languange, default en")
ap.add_argument("-2", "--lang2", default="fr",
	help="you can change the first languange, default fr")
ap.add_argument("-3", "--lang3", default="it",
	help="you can change the first languange, default it")
ap.add_argument("-4", "--lang4", default="es",
	help="you can change the first languange, default es")
ap.add_argument("-t", "--time", default=int(3),
	help="Time between one language and another, example in secondo 6.0 or 7.0 or 8.0 etc")			
				

args = vars(ap.parse_args())

if not os.path.exists('audio'):
	os.makedirs('audio')
	
if not os.path.exists('text'):
	os.makedirs('text')	

translator =  Translator()
###interrupt all def or while cicle with CTRL-C

def signal_handler(signal, frame):
    print("\nprogram exiting gracefully")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

sentence = ""
sentence1 = ""

try:
	while (sentence != "xxx"):
		
		sentence = input('insert the phrase \n xxx to exit: ')
		sentence1 = str(sentence)
		rigatransEN = translator.translate(sentence1, dest=str(args["lang1"]))
		#print(rigatransEN)
		rigatransFR = translator.translate(sentence1, dest=str(args["lang2"]))
		#print(rigatransFR)
		rigatransIT = translator.translate(sentence1, dest=str(args["lang3"]))
		#print(rigatransIT)
		rigatransES = translator.translate(sentence1, dest=str(args["lang4"]))
		#print(rigatransES)
		
		print("traduct origin: "+sentence1)
		print("             ")		
		print("traduct destination "+str(args["lang1"])+" : "+rigatransEN.text)
		
		filenameEN = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))+"_"+str(args["lang1"])+".csv"
		filenameEN = open("text"+"/"+filenameEN, "w")
		rigatransENencod = rigatransEN.text.encode('utf8', 'replace')
		filenameEN.write(str(rigatransENencod)+"\n" )
		filenameEN.close()
		
		filenameEN1 = open("text/translate_"+str(args["lang1"])+".txt", "a")
		filenameEN1.write(str(rigatransENencod)+"\n" )
		filenameEN1.close()
		
		print("             ")
		
		print("traduct destination "+str(args["lang2"])+" : "+rigatransFR.text)
		
		filenameFR = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))+"_"+str(args["lang2"])+".csv"
		filenameFR = open("text"+"/"+filenameFR, "w")
		rigatransFRencod = rigatransFR.text.encode('utf8', 'replace')
		filenameFR.write(str(rigatransFRencod)+"\n")
		filenameFR.close()
						
		filenameFR1 = open("text/translate_"+str(args["lang2"])+".txt", "a")
		filenameFR1.write(str(rigatransFRencod)+"\n" )
		filenameFR1.close()
		
		print("             ")
		print("traduct destination "+str(args["lang3"])+" : "+rigatransIT.text)
		
		filenameIT = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))+"_"+str(args["lang3"])+".csv"
		filenameIT = open("text"+"/"+filenameIT, "w")
		rigatransITencod = rigatransIT.text.encode('utf8', 'replace')
		filenameIT.write(str(rigatransITencod)+"\n")
		filenameIT.close()
				
		filenameIT1 = open("text/translate_"+str(args["lang3"])+".txt", "a")
		filenameIT1.write(str(rigatransITencod)+"\n" )
		filenameIT1.close()
				
		print("             ")
		print("traduct destination "+str(args["lang4"])+" : "+rigatransES.text)
		
		filenameES = str(datetime.now().strftime("%Y_%m_%d_%H_%M_%S"))+"_"+str(args["lang4"])+".csv"
		filenameES = open("text"+"/"+filenameES, "w")
		rigatransESencod = rigatransES.text.encode('utf8', 'replace')
		filenameES.write(str(rigatransESencod)+"\n")
		filenameES.close()
				
		filenameES1 = open("text/translate_"+str(args["lang4"])+".txt", "a")
		filenameES1.write(str(rigatransESencod)+"\n" )
		filenameES1.close()
		

		filename = datetime.now().strftime("%Y_%m_%d_%H_%M_%S") +'_eng.mp3'
		#command = "flite -o "+"audio/"+filename+" -t "+"\""+(rigatransEN.text)+"\""
		#subprocess.Popen(command, shell=True)


except KeyboardInterrupt:

	print('interrupted!')

command = "cowthink -f daemon 'CHECKMATE TO TRANSLATE IN PYTHON By Visi@n'"
subprocess.Popen(command, shell=True)
exit
