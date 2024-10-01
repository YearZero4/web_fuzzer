#!/bin/bash

# HERRAMIENTA PARA HACER FUZZING WEB #

G='\033[1;32m'
R='\033[1;31m'
W='\033[1;37m'
g='\033[7;37m'
d='\033[0;37m'
x99='/dev/null'
n=1 ; xx=0
found='resultados_fuzzing.txt'
rm $found 2>$x99

clear && echo -e "$G" && cat .banner && echo -e "$d"
if [ "$#" -ne 2 ]; then
echo -e "${R}Uso: bash $0 <URL> <dicionario>${W}"
echo -e "${d}Ejemplo: bash $0 http://ejemplo.com diccionario.txt${W}"
exit 1
fi

if [ -f $2 ];then
:
else
echo "Dicionario: $2 No existe"
exit 1
fi

cat "$2" | while read z; do
if [[ $z != '' ]];then
url="$1/${z}"
response=$(curl -Is "$url" | head -n 1)
if [[ $response == *"200"* || $response == *"301"* ]]; then
echo -e "${g}[$n]\033[0m$G Existe->$W ${z}\033[0m"
echo -e "${url}\n">>$found
((xx++))
else
echo -e "${g}[$n]\033[0m$R Error->$W ${z}\033[0m"
fi
fi
((n=$n+1))
done

if [[ $xx == 0 ]];then
echo -e "\nSe han encontrado rutas activas, se guardo\nEn $found"
fi
