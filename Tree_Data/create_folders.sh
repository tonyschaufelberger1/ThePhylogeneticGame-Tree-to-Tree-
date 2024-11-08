#!/bin/bash
i=0
for filename in ./*; do
    mkdir "$i"
	mv $filename "./$i/$filename"
    ((i++))
done

