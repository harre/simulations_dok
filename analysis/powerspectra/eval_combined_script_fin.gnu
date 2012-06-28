set terminal postscript landscape enhanced color 
set output 'fin_powspec_combined_128_h100.ps'
set xlabel 'Wavenumber k/kny'
set ylabel 'Power(k)'
set xrange[0.01:1]
set title 'Power Spectra for final snapshots, Resolution: 128'
set logscale y
set logscale x
set pointsize 10
set key font ',5' 
set key outside horiz center spacing 0.2
plot 'powspec_z33.dat' using 1:2 with lines, 'powspec_197_128_h100_drdx_3.dat' using (2*$1/128):4 with lines, 'powspec_197_128_h100_drdx_h100_r128_1.dat' using (2*$1/128):4 with lines, 'powspec_197_128_h100_drdx_h100_r128_2.dat' using (2*$1/128):4 with lines, 'powspec_197_128_h100_drkltest+3c+sl50_1.dat' using (2*$1/128):4 with lines 