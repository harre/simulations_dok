set title "Maximal virialized masses from Rockstar" 
set logscale y
set yrange [5E13:5E15]
unset key
set xtics nomirror rotate by -90 font ",8"
set terminal postscript
set output 'comparison_mvirmax.ps'
plot 'heaviestclumps_r256_h100.txt' using 2:xtic(1), 'heaviestclumps_r128_h70.txt'  using 2:xtic(1), 'heaviestclumps_r512_h100.txt' using 2:xtic(1), 'heaviestclumps_r256_h70.txt'  using 2:xtic(1)