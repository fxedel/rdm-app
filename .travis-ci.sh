#!/bin/bash
if [[ $TASK = 'nosetests' ]]; then
    nosetests --verbosity=3 --detailed-errors
elif [[ $TASK = 'karma' ]]; then
    export DISPLAY=:99.0
    sh -e /etc/init.d/xvfb start
    grunt --verbose unit-test
elif [[ $TASK = 'js-lint' ]]; then
    grunt --verbose lint
elif [[ $TASK = 'data-check' ]]; then
    ./tools/make_manufacturer_data.sh > data/manufacturer_data.py && git diff --exit-code data/manufacturer_data.py
elif [[ $TASK = 'spellintian' ]]; then
  # run the spellchecker only if it is the requested task
  spellingfiles=$(find ./ -type f -and ! \( \
      -wholename "./.git/*" -or \
      \) | xargs)
  # count the number of spellchecker errors
  spellingerrors=$(zrun spellintian $spellingfiles 2>&1 | wc -l)
  if [[ $spellingerrors -ne 0 ]]; then
    # print the output for info
    zrun spellintian $spellingfiles
    echo "Found $spellingerrors spelling errors"
    exit 1;
  else
    echo "Found $spellingerrors spelling errors"
  fi;
fi
