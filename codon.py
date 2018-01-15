strDNA = "AAATGGACTCCGTAGGATGA"
senseDNA = ""
mRNA = []
tRNA = []

def transcribe(arrDNA):
    str_mRNA = ""
    errorVal = 0
    for nucleotide in strDNA:
        errorVal += 1
        if(errorVal >= 500):
            return "Infinite Loop"
        if(nucleotide == "T"):
            str_mRNA = str_mRNA + "A"
        elif(nucleotide == "A"):
            str_mRNA = str_mRNA + "U"
        elif(nucleotide == "C"):
            str_mRNA = str_mRNA + "G"
        elif(nucleotide == "G"):
            str_mRNA = str_mRNA + "C"
    return(str_mRNA)

def smart_mRNA(strDNA):
    tempStr = transcribe(strDNA)
    tempArr = []
    presentCodon = ""
    boolean = False
    while boolean is not True:
        startCodon = tempStr[0] + tempStr[1] + tempStr[2]
        if(startCodon == 'AUG'):
            boolean = True
        else:
            tempStr = tempStr[1:]
    while len(tempStr) >= 3:
        tempArr.append("" + tempStr[0] + tempStr[1] + tempStr[2])
        tempStr = tempStr[3:]
    return(tempArr)

def tRNA(strDNA):
    tempStr = ""
    tempArr = []
    presentAntiCodon = ""
    for nucleotide in strDNA:
        if(nucleotide == "T"):
            tempStr = tempStr + "U"
        else:
            tempStr = tempStr + nucleotide
    boolean = False
    while boolean is False and len(tempStr) >= 3:
        startCodon = tempStr[0] + tempStr[1] + tempStr[2]
        if(startCodon == 'UAC'):
            boolean = True
        else:
            tempStr = tempStr[1:]
    errorVar = 0
    while len(tempStr) >= 3:
        errorVar += 1
        if errorVar > 500:
            return("Infinite Loop Error")
        tempArr.append((tempStr[0] + tempStr[1] + tempStr[2]))
        tempStr = tempStr[3:]
    return(tempArr)
def aminoAcid(strDNA):
    #AminoAcid Codon Table Below:
    Phe = ['UUU', 'UUC']
    Leu = ['UUA','UUG','CUU','CUC','CUA','CUG']
    Ile = ['AUU','AUC','AUA']
    Met = ['AUG']
    Val = ['GUU', 'GUC', 'GUA','GUG']
    Ser = ['UCU','UCC','UCA','UCG','AGU','AGC']
    Pro = ['CCU','CCC','CCA','CCG']
    Thr = ['ACU','ACC','ACA','ACG']
    Ala = ['GCU','GCC','GCA','GCG']
    Tyr = ['UAU','UAC']
    Stop = ['UAA','UAG','UGA']
    His = ['CAU','CAC']
    Gin = ['CAA','CAG']
    Asn = ['AAU','AAC']
    Lys = ['AAA','AAG']
    Asp = ['GAU','GAC']
    Glu = ['GAA','GAG']
    Cys = ['UGU','UGC']
    Trp = ['UGG']
    Arg = ['CGU','CGC','CGA','CGG','AGA','AGG']
    Gly = ['GGU','GGC','GGA','GGG']
    #Code Below:
    ls_mRNA = smart_mRNA(strDNA)
    polypeptide = ""
    for cdn in ls_mRNA:
        if(cdn in Phe):
            polypeptide = polypeptide + ('Phe-')
        elif(cdn in Leu):
            polypeptide = polypeptide + ('Leu-')
        elif(cdn in Ile):
            polypeptide = polypeptide + ('Ile-')
        elif(cdn in Met):
            polypeptide = polypeptide + ('Met-')    
        elif(cdn in Val):
            polypeptide = polypeptide + ('Val-')
        elif(cdn in Ser):
            polypeptide = polypeptide + ('Ser-')
        elif(cdn in Pro):
            polypeptide = polypeptide + ('Pro-')
        elif(cdn in Thr):
            polypeptide = polypeptide + ('Thr-')
        elif(cdn in Ala):
            polypeptide = polypeptide + ('Ala-')
        elif(cdn in Tyr):
            polypeptide = polypeptide + ('Tyr-')
        elif(cdn in Stop):
            polypeptide = polypeptide + ('Stop-')
        elif(cdn in His):
            polypeptide = polypeptide + ('His-')
        elif(cdn in Gin):
            polypeptide = polypeptide + ('Gin-')
        elif(cdn in Asn):
            polypeptide = polypeptide + ('Asn-')
        elif(cdn in Lys):
            polypeptide = polypeptide + ('Lys-')
        elif(cdn in Asp):
            polypeptide = polypeptide + ('Asp-')
        elif(cdn in Glu):
            polypeptide = polypeptide + ('Glu-')
        elif(cdn in Cys):
            polypeptide = polypeptide + ('Cys-')
        elif(cdn in Trp):
            polypeptide = polypeptide + ('Trp-')
        elif(cdn in Arg):
            polypeptide = polypeptide + ('Arg-')
        elif(cdn in Gly):
            polypeptide = polypeptide + ('Gly-')
    return polypeptide        
#For Better Copy&Paste
def printCodons(strDNA):
    tempStr = transcribe(strDNA)
    tempArr = []
    presentCodon = ""
    boolean = False
    while boolean is not True:
        startCodon = tempStr[0] + tempStr[1] + tempStr[2]
        if(startCodon == 'AUG'):
            boolean = True
        else:
            tempStr = tempStr[1:]
    while len(tempStr) >= 3:
        tempArr.append("" + tempStr[0] + tempStr[1] + tempStr[2])
        tempStr = tempStr[3:]
    for codon in tempArr:
        presentCodon = presentCodon + codon + "-"
    return(presentCodon)
def printAntiCodons(strDNA):
    tempStr = ""
    tempArr = []
    presentAntiCodon = ""
    for nucleotide in strDNA:
        if(nucleotide == "T"):
            tempStr = tempStr + "U"
        else:
            tempStr = tempStr + nucleotide
    boolean = False
    while boolean is False and len(tempStr) >= 3:
        startCodon = tempStr[0] + tempStr[1] + tempStr[2]
        if(startCodon == 'UAC'):
            boolean = True
        else:
            tempStr = tempStr[1:]
    errorVar = 0
    while len(tempStr) >= 3:
        errorVar += 1
        if errorVar > 500:
            return("Infinite Loop Error")
        tempArr.append((tempStr[0] + tempStr[1] + tempStr[2]))
        tempStr = tempStr[3:]
    for antiCodon in tempArr:
        presentAntiCodon = presentAntiCodon + antiCodon + "-"    
    return(presentAntiCodon)
def smart_mRNA(strDNA):
    tempStr = transcribe(strDNA)
    tempArr = []
    presentCodon = ""
    boolean = False
    while boolean is not True:
        startCodon = tempStr[0] + tempStr[1] + tempStr[2]
        if(startCodon == 'AUG'):
            boolean = True
        else:
            tempStr = tempStr[1:]
    while len(tempStr) >= 3:
        tempArr.append("" + tempStr[0] + tempStr[1] + tempStr[2])
        tempStr = tempStr[3:]
    return(tempArr)

def tRNA(strDNA):
    tempStr = ""
    tempArr = []
    presentAntiCodon = ""
    for nucleotide in strDNA:
        if(nucleotide == "T"):
            tempStr = tempStr + "U"
        else:
            tempStr = tempStr + nucleotide
    boolean = False
    while boolean is False and len(tempStr) >= 3:
        startCodon = tempStr[0] + tempStr[1] + tempStr[2]
        if(startCodon == 'UAC'):
            boolean = True
        else:
            tempStr = tempStr[1:]
    errorVar = 0
    while len(tempStr) >= 3:
        errorVar += 1
        if errorVar > 500:
            return("Infinite Loop Error")
        tempArr.append((tempStr[0] + tempStr[1] + tempStr[2]))
        tempStr = tempStr[3:]
    return(tempArr)
def aminoAcid(strDNA):
    #AminoAcid Codon Table Below:
    Phe = ['UUU', 'UUC']
    Leu = ['UUA','UUG','CUU','CUC','CUA','CUG']
    Ile = ['AUU','AUC','AUA']
    Met = ['AUG']
    Val = ['GUU', 'GUC', 'GUA','GUG']
    Ser = ['UCU','UCC','UCA','UCG','AGU','AGC']
    Pro = ['CCU','CCC','CCA','CCG']
    Thr = ['ACU','ACC','ACA','ACG']
    Ala = ['GCU','GCC','GCA','GCG']
    Tyr = ['UAU','UAC']
    Stop = ['UAA','UAG','UGA']
    His = ['CAU','CAC']
    Gin = ['CAA','CAG']
    Asn = ['AAU','AAC']
    Lys = ['AAA','AAG']
    Asp = ['GAU','GAC']
    Glu = ['GAA','GAG']
    Cys = ['UGU','UGC']
    Trp = ['UGG']
    Arg = ['CGU','CGC','CGA','CGG','AGA','AGG']
    Gly = ['GGU','GGC','GGA','GGG']
    #Code Below:
    ls_mRNA = smart_mRNA(strDNA)
    polypeptide = ""
    for cdn in ls_mRNA:
        if(cdn in Phe):
            polypeptide = polypeptide + ('Phe-')
        elif(cdn in Leu):
            polypeptide = polypeptide + ('Leu-')
        elif(cdn in Ile):
            polypeptide = polypeptide + ('Ile-')
        elif(cdn in Met):
            polypeptide = polypeptide + ('Met-')    
        elif(cdn in Val):
            polypeptide = polypeptide + ('Val-')
        elif(cdn in Ser):
            polypeptide = polypeptide + ('Ser-')
        elif(cdn in Pro):
            polypeptide = polypeptide + ('Pro-')
        elif(cdn in Thr):
            polypeptide = polypeptide + ('Thr-')
        elif(cdn in Ala):
            polypeptide = polypeptide + ('Ala-')
        elif(cdn in Tyr):
            polypeptide = polypeptide + ('Tyr-')
        elif(cdn in Stop):
            polypeptide = polypeptide + ('Stop-')
        elif(cdn in His):
            polypeptide = polypeptide + ('His-')
        elif(cdn in Gin):
            polypeptide = polypeptide + ('Gin-')
        elif(cdn in Asn):
            polypeptide = polypeptide + ('Asn-')
        elif(cdn in Lys):
            polypeptide = polypeptide + ('Lys-')
        elif(cdn in Asp):
            polypeptide = polypeptide + ('Asp-')
        elif(cdn in Glu):
            polypeptide = polypeptide + ('Glu-')
        elif(cdn in Cys):
            polypeptide = polypeptide + ('Cys-')
        elif(cdn in Trp):
            polypeptide = polypeptide + ('Trp-')
        elif(cdn in Arg):
            polypeptide = polypeptide + ('Arg-')
        elif(cdn in Gly):
            polypeptide = polypeptide + ('Gly-')
    return polypeptide        
def bad_mRNA_to_Codons(strMrna):
    #AminoAcid Codon Table Below:
    Phe = ['UUU', 'UUC']
    Leu = ['UUA','UUG','CUU','CUC','CUA','CUG']
    Ile = ['AUU','AUC','AUA']
    Met = ['AUG']
    Val = ['GUU', 'GUC', 'GUA','GUG']
    Ser = ['UCU','UCC','UCA','UCG','AGU','AGC']
    Pro = ['CCU','CCC','CCA','CCG']
    Thr = ['ACU','ACC','ACA','ACG']
    Ala = ['GCU','GCC','GCA','GCG']
    Tyr = ['UAU','UAC']
    Stop = ['UAA','UAG','UGA']
    His = ['CAU','CAC']
    Gin = ['CAA','CAG']
    Asn = ['AAU','AAC']
    Lys = ['AAA','AAG']
    Asp = ['GAU','GAC']
    Glu = ['GAA','GAG']
    Cys = ['UGU','UGC']
    Trp = ['UGG']
    Arg = ['CGU','CGC','CGA','CGG','AGA','AGG']
    Gly = ['GGU','GGC','GGA','GGG']
    #Code Below:
    ls_mRNA = strMrna
    polypeptide = ""
    for cdn in ls_mRNA:
        if(cdn in Phe):
            polypeptide = polypeptide + ('Phe-')
        elif(cdn in Leu):
            polypeptide = polypeptide + ('Leu-')
        elif(cdn in Ile):
            polypeptide = polypeptide + ('Ile-')
        elif(cdn in Met):
            polypeptide = polypeptide + ('Met-')    
        elif(cdn in Val):
            polypeptide = polypeptide + ('Val-')
        elif(cdn in Ser):
            polypeptide = polypeptide + ('Ser-')
        elif(cdn in Pro):
            polypeptide = polypeptide + ('Pro-')
        elif(cdn in Thr):
            polypeptide = polypeptide + ('Thr-')
        elif(cdn in Ala):
            polypeptide = polypeptide + ('Ala-')
        elif(cdn in Tyr):
            polypeptide = polypeptide + ('Tyr-')
        elif(cdn in Stop):
            polypeptide = polypeptide + ('Stop-')
        elif(cdn in His):
            polypeptide = polypeptide + ('His-')
        elif(cdn in Gin):
            polypeptide = polypeptide + ('Gin-')
        elif(cdn in Asn):
            polypeptide = polypeptide + ('Asn-')
        elif(cdn in Lys):
            polypeptide = polypeptide + ('Lys-')
        elif(cdn in Asp):
            polypeptide = polypeptide + ('Asp-')
        elif(cdn in Glu):
            polypeptide = polypeptide + ('Glu-')
        elif(cdn in Cys):
            polypeptide = polypeptide + ('Cys-')
        elif(cdn in Trp):
            polypeptide = polypeptide + ('Trp-')
        elif(cdn in Arg):
            polypeptide = polypeptide + ('Arg-')
        elif(cdn in Gly):
            polypeptide = polypeptide + ('Gly-')
    return polypeptide

#print("DNA: " + strDNA)
print("mRNA: " + transcribe(strDNA))
print("mRNA Codons: " + printCodons(strDNA))
#print("tRNA Anticodons: " + printAntiCodons(strDNA))
#print(aminoAcid(strDNA))
#print(bad_mRNA_to_Codons(['CAG','GAA','UUG','CUC','GAU']))