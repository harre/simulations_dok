#/bin/bash 

#A script that takes two arguments, a line of text and a filename
#and adds to the file of filename with the line of text at the bigenning.

cp *.tex build 
cp build/* .

cp Header.tex Notes_Single.tex
cp Header.tex Sim_r128_Single.tex 
cp Header.tex Sim_r256_Single.tex 
cp Header.tex Sim_r512_Single.tex 

location=$(pwd)

sed "s/tempopart/Notes/g" -i  Notes_Single.tex
sed "s/tempopart/r128 Simulations/g" -i  Sim_r128_Single.tex
sed "s/tempopart/r256 Simulations/g" -i  Sim_r256_Single.tex
sed "s/tempopart/r512 Simulations/g" -i  Sim_r512_Single.tex

sed "s/\chapter{Simulations}//g" -i  Notes_Single.tex
sed "s/\chapter{Simulations}//g" -i  Sim_r128_Single.tex

cat $location/Notes.tex >> $location/Notes_Single.tex  
cat $location/Sim_r128.tex >> $location/Sim_r128_Single.tex   
cat $location/Sim_r256.tex >> $location/Sim_r256_Single.tex 
cat $location/Sim_r512.tex >> $location/Sim_r512_Single.tex 

cat $location/end.tex >> $location/Notes_Single.tex  
cat $location/end.tex >> $location/Sim_r128_Single.tex   
cat $location/end.tex >> $location/Sim_r256_Single.tex 
cat $location/end.tex >> $location/Sim_r512_Single.tex 

pdflatex Notes_Single.tex 
pdflatex Sim_r128_Single.tex 
pdflatex Sim_r256_Single.tex 
pdflatex Sim_r512_Single.tex 

pdflatex Documentation.tex 

cp *.tex build 
mv *.toc *.aux *.log *.out build 
rm *_Single.tex Header.tex 