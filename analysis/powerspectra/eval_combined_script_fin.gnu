set terminal postscript landscape enhanced color 
set output 'fin_powspec_combined_256_h70.ps'
set xlabel 'Wavenumber k/kny'
set ylabel 'Power(k)'
set xrange[0.01:1E5]
set title 'Power Spectra for final snapshots, Resolution: 256'
set logscale y
set logscale x
set pointsize 10
set key font ',5' 
set key outside horiz center spacing 0.2
plot 'powspec_z0.dat' using ($1):($4*(0.703*0.703*0.226)) with lines, 'powspec_197_256_h70_cos_un_1.dat' using ($1):4 with lines, 'powspec_197_256_h70_cos_un_2.dat' using ($1):4 with lines, 'powspec_197_256_h70_cos_un_3.dat' using ($1):4 with lines, 'powspec_197_256_h70_mu_100h70_8-514200.dat' using ($1):4 with lines, 'powspec_197_256_h70_mu_100h70_8-514200_bbks.dat' using ($1):4 with lines, 'powspec_197_256_h70_mu_100h70_8-615155.dat' using ($1):4 with lines, 'powspec_197_256_h70_mu_100h70_8-711423.dat' using ($1):4 with lines, 'powspec_197_256_h70_MUSIC_3.dat' using ($1):4 with lines, 'powspec_197_256_h70_MUSIC_4.dat' using ($1):4 with lines, 'powspec_197_256_h70_nestages12.dat' using ($1):4 with lines, 'powspec_197_256_h70_nestages12_SLtest.dat' using ($1):4 with lines, 'powspec_197_256_h70_NGenIC_10629.dat' using ($1):4 with lines, 'powspec_197_256_h70_NGenIC_12206.dat' using ($1):4 with lines, 'powspec_197_256_h70_NGenIC_31954.dat' using ($1):4 with lines, 'powspec_197_256_h70_red_st14_log1.dat' using ($1):4 with lines, 'powspec_197_256_h70_red_st14_log2.dat' using ($1):4 with lines, 'powspec_197_256_h70_rst14lg3.dat' using ($1):4 with lines, 'powspec_197_256_h70_rst14log4.dat' using ($1):4 with lines, 'powspec_197_256_h70_stages_14.dat' using ($1):4 with lines 