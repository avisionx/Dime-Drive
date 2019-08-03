import final 
import revfinal

source = "IIT Delhi Main Building"
destination ="Mall of India"
json1 = final.func(source, destination)
print()
print("A.", json1)
json2 = revfinal.func(source, destination)
print("B. ", json2)
print(str(json1+json2))