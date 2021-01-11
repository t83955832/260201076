class DNA:

    dna_string = ""
    def __init__(self, dna_string):
        self.set_dna_string(dna_string)
    def get_dna_string(self):

        return self.dna_string
    def set_dna_string(self, dna_string):

        self.dna_string = dna_string

    def count_nucleotides(self):
        dna_dic = {"A":0,"T":0,"C":0,"G":0}
        for char in self.dna_string:
            dna_dic[char]+=1
        return dna_dic

    def calculate_complement(self):
        dna_dic = {"A":0,"T":0,"C":0,"G":0}​​
        reversed_dna = self.dna_string[::-1]

        complement_dna = ""

        for char in reversed_dna:

            complement_dna= complement_dna + complement_dic[char]

        return DNA(complement_dna)



dna = DNA("ATGCA")

print(dna.count_nucleotides())



complement_dna = dna.calculate_complement()

print(complement_dna.get_dna_string())
        