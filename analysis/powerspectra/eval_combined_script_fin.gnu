set terminal postscript landscape enhanced color 
set output 'fin_powspec_combined_512_h100.ps'
set xlabel 'Wavenumber k/kny'
set ylabel 'Power(k)'
set xrange[0.01:1E5]
set title 'Power Spectra for final snapshots, Resolution: 512'
set logscale y
set logscale x
set pointsize 10
set key font ',5' 
set key outside horiz center spacing 0.2
plot 'powspec_z0.dat' using ($1):($4*(0.703*0.703*0.226)) with lines, 'powspec_197_512_h100_graf-unc_100Mpc_512.dat' using ($1):4 with lines, 'powspec_197_512_h100_NGenIC_10936.dat' using ($1):4 with lines, 'powspec_197_512_h100_NGenIC_11410.dat' using ($1):4 with lines, 'powspec_197_512_h100_NGenIC_27036.dat' using ($1):4 with lines, 'powspec_197_512_h100_NGenIC_7755.dat' using ($1):4 with lines 