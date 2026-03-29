def hammimg_distance() :
    while True :
     first_string = input("Enter the 1st string sequence :").upper()
     new_first_string= "".join(first_string.split())
     valid_sequence = set(["A","T","G","C"])
     if not set(new_first_string).issubset(valid_sequence) :
        print("Wrong sequence entered")
        continue
     else :
         second_string = input("Enter the 2nd string sequence :").upper()
         new_second_string= "".join(second_string.split())
         valid_sequence = set(["A","T","G","C"])
         if not set(new_second_string).issubset(valid_sequence) :
           print("Wrong sequence entered")
           continue
         elif len(new_first_string) != len(new_second_string) :
           print("wong sequence entered.Two sequences must be of same length")
           continue
         else:
           mismatch=[]
           for i, (n1,n2) in enumerate(zip(new_first_string,new_second_string),start= 1) :
              if n1 != n2 :
                mismatch.append(i)
           total= len(mismatch)
         print(f"Hamming sequnce present at {mismatch} positions")
         print(f"total hamming sequences are : {total}")
     break
hammimg_distance()
     
        