#!/bin/bash

if test ! -d "./Assets.zip"
then
    mkdir ../Assets
    cp -r ./ ../Assets
    mv ../Assets ./
    zip -r ./Assets.zip ./Assets
    rm -rf ./Assets
fi
