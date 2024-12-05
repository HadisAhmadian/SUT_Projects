using COBREXA

	   
function loadmyModel(name)
	!isfile(name) &&
		download(string("http://bigg.ucsd.edu/static/models/",name), name);
	model = load_model(StandardModel, name)
  
	for r in model.reactions
        r[2].ub=1000000
	end
  
	for r in model.reactions
		r[2].lb=ifelse(r[2].lb<0,-1000000,0)
	end

	for r in ["EX_fru_e","EX_fum_e","EX_gln__L_e","EX_mal__L_e","FRUpts2","FUMt2_2","GLNabc","MALt2_2"]
		 remove_reaction!(model,r)
	end
  
	return model
end

loadmyModel("e_coli_core.json")