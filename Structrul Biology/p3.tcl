proc H_bond {id} {

set fp [open "H-bond-info.txt" w+] 
set var [list]

set s [measure hbonds 20 3.4 [atomselect $id all]]
foreach e $s { lappend var $e }
set a "index "

puts $fp "\n************\nDonors:"
set b [lindex $var 0]
puts $fp "name resid resname structure phi psi :"
puts $fp [[atomselect $id $a$b] get {name resid resname structure phi psi}]


puts $fp "rgyr"
puts $fp [measure rgyr [atomselect $id $a$b]]


puts $fp "\n************\nAcceptors:"
set b [lindex $var 1]
puts $fp "name resid resname structure phi psi :"
puts $fp [[atomselect $id $a$b] get {name resid resname structure phi psi}]

puts $fp "rgyr"
puts $fp [measure rgyr [atomselect $id $a$b]]


puts $fp "\n************\nHydrogens:"
set b [lindex $var 2]
puts $fp "name resid resname structure phi psi :"
puts $fp [[atomselect $id $a$b] get {name resid resname structure phi psi}]

puts $fp "rgyr"
puts $fp [measure rgyr [atomselect $id $a$b]]



close $fp

}
