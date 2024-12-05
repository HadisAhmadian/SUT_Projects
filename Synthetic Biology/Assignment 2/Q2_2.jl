using COBREXA
using JuMP
using GLPK

function if_rev(m)
  n=n_reactions(m)
  rev= Array{Int}(undef, n)
  for i=1:n
    rev[i]=ifelse(m.reactions[reactions(m)[i]].lb<0,1,0)
  end
  return rev
end

function irreversable_classic(myModel,rev,blocked,R)
    S=stoichiometry(myModel)
	n=n_reactions(myModel)
	global cnt
	cnt=1
    for i=1:n
		global c
		if rev[i]==0 && (reactions(myModel)[i] in R)
			modelLP = Model(GLPK.Optimizer)
			@variable(modelLP, V[1:n])
			@objective(modelLP, Max, V[i])
			@constraint(modelLP, S*V.==0)
			@constraint(modelLP, V[i]<=1)
			@constraint(modelLP, c[i=1:n], myModel.reactions[reactions(myModel)[i]].lb<=V[i]<=myModel.reactions[reactions(myModel)[i]].ub)
			optimize!(modelLP)
			
			if 0<=value(V[i])<=0
				
				blocked[cnt]=reactions(myModel)[i]
				cnt+=1
			end
        
		end
    end
return blocked
end


  
function reversable_classic(myModel,rev,blocked,cnt,R)
  S=stoichiometry(myModel)
  n=n_reactions(myModel)

  for i=1:n
	global cnt
    if rev[i]==1 && (reactions(myModel)[i] in R)
		
      modelLP = Model(GLPK.Optimizer)
      @variable(modelLP, V[1:n])
      @objective(modelLP, Min, V[i])
      @constraint(modelLP, S*V.==0)
      @constraint(modelLP, V[i]>=-1)
      @constraint(modelLP, c[i=1:n], myModel.reactions[reactions(myModel)[i]].lb<=V[i]<=myModel.reactions[reactions(myModel)[i]].ub)
      optimize!(modelLP)

      both_v=0
      both_v=both_v+value(V[i])
      modelLP = Model(GLPK.Optimizer)
      @variable(modelLP, V[1:n])
      @objective(modelLP, Max, V[i])
      @constraint(modelLP, S*V.==0)
      @constraint(modelLP, V[i]<=1)
      @constraint(modelLP, c[i=1:n], myModel.reactions[reactions(myModel)[i]].lb<=V[i]<=myModel.reactions[reactions(myModel)[i]].ub)
      optimize!(modelLP)

      both_v=both_v+value(V[i])
      if 0<=both_v<=0
        blocked[cnt]=reactions(myModel)[i]
		cnt+=1
      end
      
    end
  end
return blocked
end

#########################################################################################




function find_blocked(m,R,blocked)
	rev=if_rev(m)
	blocked=irreversable_classic(m,rev,blocked,R)
	global jj
	jj=1
	for x in blocked
		global jj
		if x!="none"
			jj+=1
		end
	end
	blocked=reversable_classic(m,rev,blocked,jj,R)
return blocked
end





R=["ACONTb","GAPD","CS","PGK","ENO","GLCpts","PGM","EX_glc__D_e","BIOMASS_Ecoli_core_w_GAM","ACONTa"]
i=0
j=0




for r1 in R
	
	global i
	global j
	i+=1
	j=0
	for r2 in R
		local m
		j+=1
		if i!=j
			
			m=include("init_models.jl")
			m.reactions[r1].ub=0
			m.reactions[r1].lb=0
			
			blocked=Vector{String}(undef, 90)
			for j=1:90
				blocked[j]="none"
			end
			
			B=find_blocked(m,R,blocked)
			
			
			if (r2 in B) && out[i,j]==0
				out[j,i]=3
				out[i,j]=4
			end
			
			
			if (r2 in B) && out[i,j]==3
				out[j,i]=2
				out[i,j]=2
			end
			
		end
		
	end
end

out
	