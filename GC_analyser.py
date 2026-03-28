def GC_content_analyser() :
      sequences = {}
      while True :
        user_input = input("Enter the FASTA series header :").upper()         
        new_input_value = input("Enter the FASTA series :").upper()
        new_input_key = user_input.replace(">","")   
        valid_input= set(["A","T","G","C"])
        if not set(new_input_value).issubset(valid_input) :
            print("Wrong sequence entered")
            continue
        else :
         sequences[new_input_key] = new_input_value                  
         further = input("Do you have more sequences to add ?").lower()
         if further == "yes":
            continue
         else :
           gc_value= {}
           for key,sequence in sequences.items() :
               number_G= sequence.count("G")
               number_C= sequence.count("C")
               total= len(sequence)
               percent_GC= (((number_G)+(number_C))/total)*100
               gc_value[key] = percent_GC
           max_GC = max(sequences, key = gc_value.get)
           print(f"The sequence : {max_GC} has highest GC content of {gc_value[max_GC]}")
        break
GC_content_analyser()