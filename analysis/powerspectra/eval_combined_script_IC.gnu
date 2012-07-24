set terminal postscript landscape enhanced color 
set output 'IC_powspec_combined_512_h100.ps'
set xlabel 'Wavenumber k/kny'
set ylabel 'Power(k)'
set xrange[0.01:1E5]
set title 'Power Spectra for IC, Resolution: 512'
set logscale y
set logscale x
set pointsize 10
set key font ',5' 
set key outside horiz center spacing 0.2
plot 'powspec_z23.dat' using ($1):($4/(8.8*8.8*0.226)) with lines, 'powspec_z33.dat' using ($1):($4/(12.45*12.45*0.226)) with lines, 'powspec_z50.dat' using ($1):($4/(18.67*18.67*0.226)) with lines, 'powspec_000_512_h100_graf-unc_100Mpc_512.dat' using ($1):4 with lines, 'powspec_000_512_h100_NGenIC_10936.dat' using ($1):4 with lines, 'powspec_000_512_h100_NGenIC_11410.dat' using ($1):4 with lines, 'powspec_000_512_h100_NGenIC_27036.dat' using ($1):4 with lines, 'powspec_000_512_h100_NGenIC_7755.dat' using ($1):4 with lines 