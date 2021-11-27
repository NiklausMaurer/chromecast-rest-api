#!/usr/bin/env bash

main () {

  local path="$1"

  touch "$path"

  for i in {0..9}
  do
     echo "${BASHPID}-${i}" >> "$path"
     sleep 1
  done

}

main "$1"



