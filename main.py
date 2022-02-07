def read(filename):
    return open(filename, 'r', encoding='utf-8')

def write(filename):
    return open(filename, 'w', encoding='utf-8')

def readClean(filename):
    file = read(filename)
    data = file.readlines()

    for i in range(len(data)):
        data[i] = data[i].strip("\n")

    return data

def readAllData(nom='txt/inputs/data.txt'):
    data = readClean(nom)
    pseudos = []
    fiche = []
    habbo = []
    for line in data:
        split = line.split(';')
        pseudos.append(split[0])
        fiche.append(split[1])
        habbo.append(split[2])
    return pseudos, fiche, habbo
    

def writeDemandeRetro():
    #### On récupère les pseudos et les dates ####

    #pseudos = readClean('pseudos.txt') ## Ancien fonctionnement
    #fiche = readClean('fiche.txt')
    #habbo = readClean('habbo.txt')

    data = readAllData()
    pseudos = data[0]
    fiche = data[1]
    habbo = data[2]
    
    #### On récupère le modèle pour retro ####
    fileRetro = read('txt/samples/sample_retro.txt')
    sample = fileRetro.read()

    #### Enfin, on écrit les rétros puis on les écrit dans un fichier ####
    string = ""
    for i in range(len(pseudos)):
        string += sample.format(pseudos[i], fiche[i], habbo[i])

    fileFinal = write('txt/outputs/retro.txt')
    fileFinal.write(string)

def writeRetro():
    ### Même fonctionnement qu'au dessus, en plus simple
    #pseudos = readClean('pseudos.txt') ## Ancien fonctionnement
    pseudos = readAllData()[0]
    fileRetro = read('txt/samples/sample_retro_final.txt')
    sample = fileRetro.read()

    string = ""
    for i in range(len(pseudos)):
        string += sample.format(pseudos[i])

    fileFinal = write('txt/outputs/retro_final.txt')
    fileFinal.write(string)

def pseudoDump(): # Obsolete, à ne plus utiliser
    pseudos = readAllData()[0]
    string = ""
    for x in pseudos:
        string += x
        string += "\n"

    write('pseudo_dump.txt').write(string)


def writeRetraitBadge():
    pseudos = readAllData()[0]
    string = ""
    for x in pseudos:
        string += x
        string += "\n"

    sample = read('txt/samples/sample_retrait_badge.txt').read()
    write('txt/outputs/retrait_badge.txt').write(sample.format(string))

def writeUserRecap(pseudo, jour, appr):
    sample = read('txt/samples/sample_user_recap.txt').read()
    return sample.format(pseudo, jour, appr)

def writeRecap(date):
    data = readAllData('txt/inputs/data_recap.txt')
    string = ""
    for i in range(len(data[0])):
        string += writeUserRecap(data[0][i], data[1][i], data[2][i])
    sample_final = read('txt/samples/sample_recap.txt').read()
    write('txt/outputs/recap_final.txt').write(sample_final.format(date, string))
        
