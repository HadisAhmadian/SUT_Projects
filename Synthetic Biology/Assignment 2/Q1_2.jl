m=include("init_models.jl")
R=m.reactions
L=["BIOMASS_Ecoli_core_w_GAM","PGK","PGM","PIt2r","ACONTa","ACONTb","CS","RPI","ENO","EX_glc__D_e","EX_h_e","EX_nh4_e","EX_pi_e","GAPD","GLCpts","GLNS","ICDHyr","NH4t"]
VBiomass=34148.42956394258
f=0.01
global c
c=0
global i
i=1
checked=Vector{String}(undef, 90)
for j=1:90
	checked[j]="none"
end
for r1 in R
	global c
	global i
	checked[i]=r1[1]
	i+=1
	for r2 in R
		
		if !(r1[1] in L) && !(r2[1] in L)&& r1[1]!=r2[1] && !(r2[1] in checked)
			u1=r1[2].ub
			l1=r1[2].lb
			r1[2].ub=0
			r1[2].lb=0
			u2=r2[2].ub
			l2=r2[2].lb
			r2[2].ub=0
			r2[2].lb=0
			dict=flux_balance_analysis_dict(m, GLPK.Optimizer)
			
			if dict["BIOMASS_Ecoli_core_w_GAM"]<f*VBiomass
				c+=1
				print(r1[1]," and ",r2[1]," : ",dict["BIOMASS_Ecoli_core_w_GAM"],"\n")
				
			end	
			r1[2].ub=u1
			r1[2].lb=l1
			r2[2].ub=u2
			r2[2].lb=l2
		end
	end
end
print("count: ",c)