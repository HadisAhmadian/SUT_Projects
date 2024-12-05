	
R=["ACONTb","GAPD","CS","PGK","ENO","GLCpts","PGM","EX_glc__D_e","BIOMASS_Ecoli_core_w_GAM","ACONTa"]
out=zeros(Int8, 10, 10)
m=include("init_models.jl")
dict=flux_balance_analysis_dict(m, GLPK.Optimizer)

i=0
j=0
for r1 in R
	global i
	global j
	i+=1
	j=0
	for r2 in R
		j+=1
		if dict[r1]%dict[r2]==0 || dict[r2]%dict[r1]==0
			print(r1," and ",r2,"\n")
			out[i,j]=1
			out[j,i]=1
		end
	end
end
