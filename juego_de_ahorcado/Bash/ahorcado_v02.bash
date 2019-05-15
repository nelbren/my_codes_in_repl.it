#!/bin/bash
# ahorcado_v02.bash - 2019-05-13 - nelbren.com

declare -a palabras=('astrid' 'camarones' 'dormir')
declare -a letras
intentos=5

mostrar_palabras() {
  for p in ${palabras[*]}; do
    echo $p
  done
}

seleccion_de_palabra() {
  numero_palabras=${#palabras[*]}
  r=$(( $RANDOM % $numero_palabras + 1 ))
  r=$((r-1))
  palabra=${palabras[$r]}
  longitud_palabra=${#palabra}
}

seleccion_de_palabra2() {
  diccionario=/tmp/listado-general.txt
  if [ ! -r $diccionario ]; then
    #lynx https://raw.githubusercontent.com/javierarce/palabras/master/listado-general.txt --dump > $diccionario
    wget https://raw.githubusercontent.com/javierarce/palabras/master/listado-general.txt -O $diccionario
  fi

  numero_palabras=$(cat $diccionario | wc -l)
  r=$(( $RANDOM % $numero_palabras + 1 ))
  r=$((r-1))

  palabra=$(head -$r /tmp/listado-general.txt | tail -1)
  longitud_palabra=${#palabra}
}

buscar_en_anteriores() {
  numero_letras=${#letras[*]}
  for ((i=0;i<$numero_letras;i++)); do
    if [ "$letra_palabra" == "${letras[$i]}" ]; then
      existe=1 
      break
    fi
  done
}

mostrar_palabra() {
  echo -n "Tip: Es una palabra con $longitud_palabra letras : "
  completo=1
  encontrada=0

  for ((c=0;c<$longitud_palabra;c++)); do
    existe=0
    letra_palabra="${palabra:$c:1}"
    buscar_en_anteriores
    if [ "$existe" == "0" -a \
         "${palabra:$c:1}" == "$letra_usuario" ]; then
      letras[$numero_letras]=$letra_usuario
      existe=1
      encontrada=1
    fi
    if [ "$existe" == "1" ]; then
      echo -n "$letra_palabra "
    else
      echo -n "_ "
      completo=0
    fi
  done
  echo ""
}

ciclo_ahorcado() {
  while true; do
    mostrar_palabra
    if [ "$completo" == "1" ]; then
      echo "En hora buena."
      break
    else
      if [ "$encontrada" == "0" ]; then
        if [ "$intentos" -gt "0" ]; then
          intentos=$((intentos-1))
	  echo "Intentos restantes = $intentos"
        else
	  echo "Ahorcado!"
	  echo "La palabra era: $palabra"
	  break
        fi
      else 
	echo "Vas bien..."
      fi
    fi  
    echo -n "Letra: "
    read letra_usuario
  done
}

seleccion_de_palabra2
ciclo_ahorcado
