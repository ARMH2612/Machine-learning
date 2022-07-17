% Exercice 1
n = input("Enter un nembre entier N:")
result = true;

for j=1:n
    if (j == 1)
         result = false;
     elseif (j == 2)
         result = true;
     else 
        for i=2:j-1,
            if (mod(j,i)==0)
               result = false;
            end
        end
     end
    if(result)
        j
   end
end
