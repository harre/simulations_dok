set terminal postscript landscape enhanced color 
set output 'omega_evolution_256_h70.ps'
set xlabel 'Redshift'
set ylabel 'Omega Matter'
set title 'Omega Evolution, Resolution: 256'
set xrange [0:35] reverse
set pointsize 10
set key font ',5' 
set key outside horiz center spacing 0.2
plot 'omega_r256_h70_mm_h.out' using 1:2 with lines, 'omega_r256_h70_mu_100h70_8-514200.out' using 1:2 with lines, 'omega_r256_h70_mu_100h70_8-514200_bbks.out' using 1:2 with lines, 'omega_r256_h70_mu_100h70_8-711423.out' using 1:2 with lines, 'omega_r256_h70_MUSIC_1.out' using 1:2 with lines, 'omega_r256_h70_MUSIC_2.out' using 1:2 with lines, 'omega_r256_h70_MUSIC_3.out' using 1:2 with lines, 'omega_r256_h70_MUSIC_4.out' using 1:2 with lines, 'omega_r256_h70_red_st14_log1.out' using 1:2 with lines, 'omega_r256_h70_red_st14_log2.out' using 1:2 with lines, 'omega_r256_h70_rst14lg3.out' using 1:2 with lines, 'omega_r256_h70_rst14log4.out' using 1:2 with lines, 'omega_r256_h70_stages_12_h_44.out' using 1:2 with lines 