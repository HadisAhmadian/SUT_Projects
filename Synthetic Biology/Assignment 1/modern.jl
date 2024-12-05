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

function if_rev(model)
  n=model.n
  rev= Array{Int}(undef, n)
  for i=1:n
    rev[i]=ifelse(model.lb[i]<0,1,0)
  end
  
  return rev
end

function hemogen(model,M,rev)
  n=model.n
  for i=1:n
      model.ub[i]=M
      model.lb[i]=ifelse(rev[i]==1,-M,0)
  end
  return model
end

function irreversable_modern(myModel,rev)
    S=myModel.S
    n=myModel.n
	
	c=0
	for i=1:n
		c=c+ifelse(rev[i]==0,1,0)
	end
	
	irr=fill(1, c)
	j=1
	
	for i=1:n
		if rev[i]==0
			irr[j]=i
			j=j+1
		end
	end
	
	
	I=fill(1, c)
    modelLP = Model(GLPK.Optimizer)
    @variable(modelLP, V[1:n])
	@variable(modelLP, u[1:c])
    @objective(modelLP, Max,transpose(I)*u)
    @constraint(modelLP, S*V.==0)
	@constraint(modelLP, [i=1:c],V[irr[i]]>=u[i])
    @constraint(modelLP, [i=1:c],0<=u[i]<=1)
    optimize!(modelLP)
	
	
	for i in irr
		if 0<=value(V[i])<=0
			print(myModel.Reactions[i],"\n")
		end
	end
	

  end
  
 
for name in ["iNF517.json","iNJ661.json"]
#"Recon3D.json","iNF517.json","iNJ661.json","iAB_RBC_283.json","
  print(">",name,"\n")
  myModel=loadmyModel(name)
  rev=if_rev(myModel)
  M=100000
  myModel=hemogen(myModel,M,rev)
  #print(myModel)
  #print("irreversable blocked reactios MODERN approach:\n")
  irreversable_modern(myModel,rev)
  #print("********************************************************\n\n")
end