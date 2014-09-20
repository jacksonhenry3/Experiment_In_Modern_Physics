set term png enhanced
set output 'dataPlot.png'
unset key
set xlabel 'sqrt(v)/I'
set ylabel 'Diameter [cm]'
set title 'Diameter of ring of electrons in B field'
f(x)=a*x+b
fit f(x) 'finalColumnData.txt' using 7:5:6 via a,b
plot 'finalColumnData.txt' using 7:5:8:6 w xyerrorbars, f(x)

 