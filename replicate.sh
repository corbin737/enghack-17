#!/bin/bash

if test -d "./Assets"
then
echo "It exists"
else
echo "It doesn't exist"
fi

if test ! -d "./Assets"
then
    mkdir ../Assets
    cp -r ./ ../Assets
    mv ../Assets ./
fi
