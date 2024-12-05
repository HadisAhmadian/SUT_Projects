using COBREXA
using JuMP
using GLPK

struct models
           S
           Metabolites
           Reactions
           Genes
           m
           n
           lb
           ub
       end
	   
function loadmyModel(name)
  !isfile(name) &&
    download(string("http://bigg.ucsd.edu/static/models/",name), name);
  model = load_model(StandardModel, name)
  m=n_metabolites(model)
  n=n_reactions(model)
  myModel=models(stoichiometry(model),metabolites(model),reactions(model),genes(model),m,n,bounds(model)[1],bounds(model)[2])
  return myModel
end

  
open("Models.txt","w") 

for name in ["e_coli_core.json","iAB_RBC_283.json","iNF517.json","iNJ661.json"]
  print(">",name,"\n")
  myModel=loadmyModel(name)
  
  print(myModel)
  print("\n***************************************************************************\n\n")
end