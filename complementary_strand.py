def complementary() :
    sequence = input("Enter the sequence :").upper()
    correct_sequence = "".join(sequence.split())
    valid_sequence= set(["A","T","G","C"])
    if len(correct_sequence) == 0 :
        print ( f"No sequence detected")
        return
    elif not set(correct_sequence).issubset(valid_sequence) :
        print("wrong sequence entered")
        return
    else :
        complement = {
            "A" : "T",
            "T" : "A",
            "G" : "C",
            "C" : "G"
        }
        sequence_box= []
        for letter in correct_sequence :
            new_sequence= complement[letter]
            sequence_box.append(new_sequence)
        result= "".join(sequence_box)
        print(f"Your entered sequence is 5'-{correct_sequence}-3'")
        print(f" The complementary sequence is 3'-{result}-5'")
        print(f"The reverse sequence is : 5'- {result[::-1]}-3'")
complementary()
    