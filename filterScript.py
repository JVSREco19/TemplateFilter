import re

def remove_repetidos(lista):
    l = []
    removeCounter = 0;
    for i in lista:
      if i[0:len(i)-1] not in l :
        l.append(i[0:len(i)-1])
        linesToMantain.append(int(i[len(i)-1]))

      else:
        removeCounter+=1;
    
      l.sort()
    print(str(removeCounter)+ " Removed")
    return l



archiveName = 'templates_lit.txt'
if archiveName[len(archiveName)-3:len(archiveName)] =='txt' and archiveName[0:7]!='treated':
  print("Opening {} file".format(archiveName))
  ficheiro = open(archiveName)
  text = ficheiro.readlines()
  linesToMantain = []
  repeatedLines = []
  if(archiveName[-3:]=='csv'):
    text = text[2:]

  activeSites = []
  counter = 0;
  textList =[]
  for linha in text:
    words = linha.split()
    textList.append(linha.split())
    
    templateCode = words[0]
    ligationsString = words[3:]
    i = 0
    auxLigationsString = []
    while(i<len(ligationsString)):
      auxLigationsString.append(" ".join(ligationsString[i:i+2]))
      i+=3
    auxLigationsString.append(templateCode)
    activeSites.insert(counter, auxLigationsString)
    activeSites[counter].sort()
    activeSites[counter].append(str(counter))
    counter= counter +1;
  counter = 0;


  remove_repetidos(activeSites)
  
  treatedText = []

  for num in linesToMantain:
    if(counter==100):
      counter =0
    treatedLine = textList[num]
    counter += 1;
    treatedLineStr = ' '.join(treatedLine)
    treatedText.append(treatedLineStr)
    
    
  ficheiro.close()
  treatedFile = open("treated"+archiveName,"w")


  for member in treatedText:
    treatedFile.write(member+'\n')
  
  treatedFile.close()
  