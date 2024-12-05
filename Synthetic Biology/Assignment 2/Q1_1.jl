m=include("init_models.jl")
R=m.reactions
VBiomass=34148.42956394258
f=0.01
for r in R

	if r[1]!="BIOMASS_Ecoli_core_w_GAM"
		u=r[2].ub
		l=r[2].lb
		r[2].ub=0
		r[2].lb=0
		dict=flux_balance_analysis_dict(m, GLPK.Optimizer)
		if dict["BIOMASS_Ecoli_core_w_GAM"]<f*VBiomass
			print(r[1],",")
		end	
		r[2].ub=u
		r[2].lb=l
	end
end

