#Parse blast output 80pid to get 90pid and 95pid id alignments respectively for circos input format

path = "BLAST_CIRCOS/qNLB_1_25377803_22184"

filename = path+ "/Region1_Ch3vsb73v2all.txt"                              # input the blast_v2all file(blast comparison with the whole genome_global repeats)
filename2 = path+ "/Region1_Ch3vsRegion1_Ch3.txt"                          # input the blast_v2region file(blast comparison with itself_local repeats)


#filename = "test_blast_v2all.txt"
#filename2 = "test_blast_v2region.txt"

alignment_len_threshold = 1000

out_put1 = path+ "/"+ path [13:]+"_1ksegmental_duplications_global-local_90_Circos.txt"                             # output the blast_v2all file >90pid (blast comparison with the whole genome_global repeats)
out_put2 = path+ "/"+ path [13:]+"_1ksegmental_duplications_global-local_95_Circos.txt"                             # output the blast_v2all file >95pid(blast comparison with itself_local repeats)

###########global repeat######

f1 = open(filename, "r")
f2 = open (out_put1, "w")
f3 = open (out_put2, "w")

lines1 = f1.readlines()
for line in lines1:
                #print line
                line2=line.split('\n')
                line3 = line2 [0]
                cols = line3.split(',')
                cols0 = cols [0].split(':')
                cols1 = cols [1].split(':')
                if line3.startswith('chr'):
                                x = cols[2][:-1]
                                y = float(x)
                                zz = cols[3]
                                alignment_len = int(zz)
                                if y >= 90 and (alignment_len >= int(alignment_len_threshold))  and ((((int(cols [6])) != (int (cols [8]))) and ((int(cols [7])) != (int (cols [9])))) and (((int(cols [6])) != (int (cols [9]))) and ((int(cols [7])) != (int (cols [8])))) ):
                                                #print ("zm"+cols0 [2])
                                                #print ("zm"+cols1 [2])
                                                #print ("zm"+ cols0 [2] + " " + cols [6] + " " + cols [7] + " " + "zm" + cols1 [2] + " " + cols [8] + " " + cols [9])
                                                #print cols [1]
                                                f2.write (("zm"+ cols0 [2] + " " + cols [6] + " " + cols [7] + " " + "zm" + cols1 [2] + " " + cols [8] + " " + cols [9]) + "\n")
                                                
                                if y >= 95 and (alignment_len >= int(alignment_len_threshold))  and ((((int(cols [6])) != (int (cols [8]))) and ((int(cols [7])) != (int (cols [9])))) and (((int(cols [6])) != (int (cols [9]))) and ((int(cols [7])) != (int (cols [8])))) ):
                                                f3.write (("zm"+ cols0 [2] + " " + cols [6] + " " + cols [7] + " " + "zm" + cols1 [2] + " " + cols [8] + " " + cols [9]) + "\n")                
                                

f1.close()


#############local repeat######

f4 = open(filename2, "r")


lines4 = f4.readlines()
for line in lines4:
                #print line
                line5 = line.split('\n')
                line6 = line5 [0]
                cols = line6.split(',')
                cols2 = cols [0].split(':')
                cols3 = cols [1].split(':')
                if line6.startswith('chr'):
                                x = cols[2][:-1]
                                y = float(x)
                                if y >= 90 and (alignment_len >= int(alignment_len_threshold))  and ((((int(cols [6])) != (int (cols [8]))) and ((int(cols [7])) != (int (cols [9])))) and (((int(cols [6])) != (int (cols [9]))) and ((int(cols [7])) != (int (cols [8])))) ):
                                                #print ("zm"+cols0 [2])
                                                #print ("zm"+cols1 [2])
                                                #print ("zm"+ cols2 [2] + " " + cols [6] + " " + cols [7] + " " + "zm" + cols3 [2] + " " + cols [8] + " " + cols [9])
                                                f2.write (("zm"+ cols2 [2] + " " + cols [6] + " " + cols [7] + " " + "zm" + cols3 [2] + " " + cols [8] + " " + cols [9]) + "\n")
                                                
                                if y >= 95 and (alignment_len >= int(alignment_len_threshold))  and ((((int(cols [6])) != (int (cols [8]))) and ((int(cols [7])) != (int (cols [9])))) and (((int(cols [6])) != (int (cols [9]))) and ((int(cols [7])) != (int (cols [8])))) ):
                                                f3.write (("zm"+ cols2 [2] + " " + cols [6] + " " + cols [7] + " " + "zm" + cols3 [2] + " " + cols [8] + " " + cols [9]) + "\n")
f2.close()                                
f3.close()
f4.close()
