
x = -pi:pi;
y = x*sin(x)
z = x+sin(x)

figure('name','Fenetre des graphes representatif des fonctions y et z');

plot(x,y)
hold on
plot(x,z)
grid on

xlabel('-pi < x < pi') 
ylabel('x*sin(x) et x+sin(x) resultats') 

title('Graphes representatif des fonctions x*sin(x) et x+sin(x)')

hold off