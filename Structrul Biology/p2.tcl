proc RMSD-All {id} {


set fp [open "RMSD-All-info.txt" w+] 


for { set a 0}  {$a < 10} {incr a} {
   for { set b 0}  {$b < 10} {incr b} {
		puts $fp "$a and $b :"
		puts $fp [measure rmsd [atomselect $id all frame $a] [atomselect $id all frame $b]]
		puts $fp "\n"
		}
}

close $fp

}