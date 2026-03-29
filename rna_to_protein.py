def translation() :
    sequence= input("Enter the sequence :").upper()
    new_sequence = "".join(sequence.split())
    valid_sequence= set(["A","U","G","C"])
    if not set(new_sequence).issubset(valid_sequence) :
        print("Wrong sequence entered")
        return
    elif len(new_sequence)== 0 :
        print("No sequence detected")
        return
    else :
        codons=[]
        transcription_box = {
            'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',                
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', 'UAA':'Stop', 'UAG':'Stop',
    'UGC':'C', 'UGU':'C', 'UGA':'Stop', 'UGG':'W',
        }
        for i in range(0,len(new_sequence),3) :
            new=new_sequence[i:i+3]
            codons.append(new)
        protein=[]
        for codon in codons:
            if len(codon)<3 :
                break
            else :
              aminoacid=transcription_box[codon]
              if aminoacid== "Stop" :
                break
              else :
                protein.append(aminoacid)
        protein_sequence= "-".join(protein)
        print(f"The protein sequence for the given sequence will be {protein_sequence}")
translation()