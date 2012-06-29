set terminal postscript landscape enhanced color 
set output 'omega_evolution_512_h100.ps'
set xlabel 'Redshift'
set ylabel 'Omega Matter'
set title 'Omega Evolution, Resolution: 512'
set xrange [0:35] reverse
set pointsize 10
set key font ',5' 
set key outside horiz center spacing 0.2
plot 'omega_r512_h100_512er_major_merger.out' using 1:2 with lines, 'omega_r512_h100_graf-unc_100Mpc_512.out' using 1:2 with lines, 'omega_r512_h100_NGenIC_10936.out' using 1:2 with lines, 'omega_r512_h100_NGenIC_11410.out' using 1:2 with lines, 'omega_r512_h100_NGenIC_27036.out' using 1:2 with lines, 'omega_r512_h100_NGenIC_7755.out' using 1:2 with lines 