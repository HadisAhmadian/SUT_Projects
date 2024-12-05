#change directory
cd prots 
#load model
mol load pdb 1k8h.pdb 


#for better view
set id 0
mol modstyle 0 $id NewCartoon 0.300000 10.000000 4.100000 0
mol modcolor 0 $id Structure

# showing length of sequence
[atomselect $id "name CA"] num

# showing sequence of AAs
[atomselect $id "name CA"] get {resname}


# counting how many of each AA is in the sequence
set names { ALA ARG ASN ASP CYS GLU GLN GLY HIS ILE LEU LYS MET PHE PRO SER THR TRP TYR VAL }
foreach name $names { puts "$name :"
puts [[atomselect $id "name CA and resname $name" frame $a] num] }


# extracing phi and psi for every CA to use for plot (by python)
[atomselect $id "name CA"] get {phi psi}


