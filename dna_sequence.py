def seq():
    sequence=input("Enter the sequence :")
    valid_input= "".join(sequence.split())
    new_sequence= valid_input.upper()
    valid_sequence= set(["A","T","G","C"])
    if len(new_sequence) == 0 :
        print (f"no sequence found")
        return
    elif set(new_sequence).issubset(valid_sequence) :
        number_A= new_sequence.count("A")
        number_T= new_sequence.count("T")
        number_G= new_sequence.count("G")
        number_C= new_sequence.count("C")
        print(f"number of A:{number_A}")
        print(f"number of T:{number_T}")
        print(f"number of G:{number_G}")
        print(f"number of C:{number_C}")
        total_nucleotide=len(new_sequence)
        percent_AT = (((number_A)+(number_T))/total_nucleotide)*100
        percent_GC = 100 - percent_AT
        print(f"percentage of AT sequence is :{percent_AT:.2f}%")
        print(f"percentage of GC sequence is :{percent_GC:.2f}%")
    else :
        print(f" You entered a wrong sequence")
        return
seq()