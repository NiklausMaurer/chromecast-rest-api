#!/usr/bin/env bash

main () {

  local path="$1"
  local url="$2"

  touch "$path"

  for i in {0..9}
  do
     echo "${BASHPID}-${url}-${i}" >> "$path"
     sleep 1
  done

}

main "$1" "$2"



