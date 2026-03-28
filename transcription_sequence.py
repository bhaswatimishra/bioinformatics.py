def transcription() :
    coding_strand = input(f"Enter the sequence of coding strand")
    new_sequence= "".join(coding_strand.split())
    correct_sequence=new_sequence.upper()
    valid_sequence= set(["A","T","G","C"])
    if len(correct_sequence) == 0 :
        print(f"No sequence detected")
        return
    elif set(correct_sequence).issubset(valid_sequence) :
        rna_sequence= correct_sequence.replace("T","U")
        print(f"The new RNA sequence will be :\n {rna_sequence}")
    else :
        print(f"Wrong sequence entered")
        return
transcription()