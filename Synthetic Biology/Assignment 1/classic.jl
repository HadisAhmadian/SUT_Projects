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

function irreversable_classic(myModel,rev)
    S=myModel.S
    n=myModel.n
    for i=1:n
      if rev[i]==0
        modelLP = Model(GLPK.Optimizer)
        @variable(modelLP, V[1:n])
        @objective(modelLP, Max, V[i])
        @constraint(modelLP, S*V.==0)
        @constraint(modelLP, V[i]<=1)
        @constraint(modelLP, c[i=1:n], myModel.lb[i]<=V[i]<=myModel.ub[i])
        optimize!(modelLP)
        if -1e-13<=value(V[i])<=1e-13
          print(myModel.Reactions[i],"\n")
        end
        
      end
    end
  end
  
 function reversable_classic(myModel,rev)
  S=myModel.S
  n=myModel.n
  for i=1:n
    if rev[i]==1
      modelLP = Model(GLPK.Optimizer)
      @variable(modelLP, V[1:n])
      @objective(modelLP, Min, V[i])
      @constraint(modelLP, S*V.==0)
      @constraint(modelLP, V[i]>=-1)
      @constraint(modelLP, c[i=1:n], myModel.lb[i]<=V[i]<=myModel.ub[i])
      optimize!(modelLP)

      both_v=0
      both_v=both_v+value(V[i])

      modelLP = Model(GLPK.Optimizer)
      @variable(modelLP, V[1:n])
      @objective(modelLP, Max, V[i])
      @constraint(modelLP, S*V.==0)
      @constraint(modelLP, V[i]<=1)
      @constraint(modelLP, c[i=1:n], myModel.lb[i]<=V[i]<=myModel.ub[i])
      optimize!(modelLP)

      both_v=both_v+value(V[i])

      if -1e-13<=both_v<=1e-13
        print(myModel.Reactions[i],"\n")
      end
      
    end
  end
end

for name in ["iNJ661.json"]
#"Recon3D.json",,"iNF517.json","iNJ661.json"
  print(">",name,"\n")
  myModel=loadmyModel(name)
  rev=if_rev(myModel)
  M=1000000
  myModel=hemogen(myModel,M,rev)
  #print(myModel)
  print("#irreversable blocked reactios:\n")
  irreversable_classic(myModel,rev)
  print("#reversable blocked reactios:\n")
  reversable_classic(myModel,rev)
  #print("********************************************************\n\n")
end