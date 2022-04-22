def RXCD(mother_genotype : str, father_genotype : str): # Recessive X Chromosome Diseased
   if len(father_genotype) > 1:
      raise Exception("Father genotype must have only 1 word")
   if len(mother_genotype) > 2 or len(mother_genotype) == 1:
      raise Exception("Mother genotype must have only 2 words")

   # division alleles of mother and father
   from_mother1 = mother_genotype[0]
   from_father1 = father_genotype[0]
   from_mother2 = mother_genotype[-1]
   from_father2 = "0" # Male always have XY chromosome

   # merge the genotype into possibility
   result_fm1 = from_mother1+from_father1
   result_fm2 = from_mother2 + from_father1
   result_m1 = from_mother1 + from_father2
   result_m2 = from_mother2 + from_father2

   # The genotype must always startwiths "a"
   if result_fm1.startswith("a"):
      result_fm1 = result_fm1[::-1]
   if result_fm2.startswith("a"):
      result_fm2 = result_fm2[::-1]

   # assign a dictionary variable
   info1 = {"result":result_fm1, "sex":"Female", "status" : ""}
   info2 = {"result":result_fm2, "sex":"Female", "status" : ""}
   info3 = {"result":result_m1, "sex": "Male", "status" : ""}
   info4 = {"result":result_m2, "sex": "Male", "status" : ""}

   # diseased or normally or career
   # Male diseased possibility only have diseased and normally
   if 'a' in info3['result']:
      info3['status'] = "diseased"
   else:
      info3['status'] = "normally"
   if 'a' in info4['result']:
      info4['status'] = "diseased"
   else:
      info4['status'] = "normally"

   # Female diseased possibility have diseased, career and normally
   if info1['result'] == "Aa":
      info1['status'] = "career"
   elif info1['result'] == "AA":
      info1['status'] = "normally"
   elif info1['result'] == "aa":
      info1['status'] = "diseased"
   if info2['result'] == "Aa":
      info2['status'] = "career"
   elif info2['result'] == "AA":
      info2['status'] = "normally"
   elif info2['result'] == "aa":
      info2['status'] = "diseased"

   # return the value
   # return diseased of female possibility
   if (info1['status'], info2['status']) == ("normally", "normally") or (info2['status'], info1['status']) == ("normally", "normally"):
      yield {"sex":"Female", "normally": 100,"career": 0, "diseased": 0, "chromosome":"XX"}
   elif (info1['status'], info2['status']) == ("normally", "career") or (info2['status'], info1['status']) == ("normally", "career"):
      yield {"sex":"Female", "normally": 50,"career": 50, "diseased": 0, "chromosome":"XX"}
   elif (info1['status'], info2['status']) == ("diseased", "normally") or (info2['status'], info1['status']) == ("diseased", "normally"):
      yield {"sex":"Female", "normally": 0, "career": 50, "diseased": 50, "chromosome":"XX"}
   elif (info1['status'], info2['status']) == ("diseased", "diseased") or (info2['status'], info1['status']) == ("diseased", "diseased"):
      yield {"sex":"Female", "normally": 0,"career": 0, "diseased": 100, "chromosome":"XX"}
   elif (info1['status'], info2['status']) == ("career", "diseased") or (info2['status'], info1['status']) == ("career", "diseased"):
      yield {"sex":"Female", "normally": 0,"career": 50, "diseased": 50, "chromosome":"XX"}
   elif (info1['status'], info2['status']) == ("career", "career") or (info2['status'], info1['status']) == ("career", "career"):
      yield {"sex":"Female", "normally": 0,"career": 100, "diseased": 0, "chromosome":"XX"}

   # Return diseased of male possibility
   if (info3['result'], info4['result']) == ("A0","a0") or (info4['result'], info3['result']) == ("A0","a0"):
      yield {"sex": "Male", "normally": 50, "diseased": 50, "chromosome":"XY"}
   elif (info3['result'], info4['result']) == ("A0","A0") or (info4['result'], info3['result']) == ("A0","A0"):
      yield {"sex": "Male", "normally": 100, "diseased": 0, "chromosome":"XY"}
   elif (info3['result'], info4['result']) == ("a0","a0") or (info4['result'], info3['result']) == ("a0","a0"):
      yield {"sex": "Male", "normally": 0, "diseased": 100, "chromosome":"XY"}

# Example
if __name__ == "__main__":
   m = str(input("Enter Allele of a mother (Example = AA, Aa, aa)\t: ")) # Can input only 2 len
   f = str(input("Enter Allele of a father (Example = A, a)\t\t: ")) # Can input only 1 len
   result = RXCD(m, f)
   print(next(result))
   print(next(result))
