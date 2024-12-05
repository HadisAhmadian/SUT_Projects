proc frame_struct {id} {


set fp [open "frame_struct_info.txt" w+] 


for { set a 0}  {$a < 10} {incr a} {


   puts $fp "\nFRAME $a :"
   set selection [atomselect $id "name CA" frame $a]
   set s [$selection get {structure}]
   set count [[atomselect $id "name CA" frame $a] num]
   puts $fp $s
   

   set n [[atomselect $id "name CA and structure C" frame $a] num]
   puts $fp "C: $n / $count "
   
   set n [[atomselect $id "name CA and structure E" frame $a] num]
   puts $fp "E: $n / $count "
   
   set n [[atomselect $id "name CA and structure T" frame $a] num]
   puts $fp "T: $n / $count "
   
   set n [[atomselect $id "name CA and structure H" frame $a] num]
   puts $fp "H: $n / $count "
   
   set n [[atomselect $id "name CA and structure G" frame $a] num]
   puts $fp "G: $n / $count "
   
   set n [[atomselect $id "name CA and structure I" frame $a] num]
   puts $fp "I: $n / $count "
   
   set n [[atomselect $id "name CA and structure B" frame $a] num]
   puts $fp "B: $n / $count "
   
   set n [[atomselect $id "name CA and structure S" frame $a] num]
   puts $fp "S: $n / $count "
   
   
}

close $fp

}