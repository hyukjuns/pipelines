#!/bin/bash

# BLUE: 80 -> 8081
az network lb rule update -g "rg-packer" --lb-name "vmss-lb" -n $1 --frontend-port "8081" --protocol "Tcp"

# GREEN: 8080 -> 80
az network lb rule update -g "rg-packer" --lb-name "vmss-lb" -n $2 --frontend-port "80" --protocol "Tcp"

# BLUE: 8081 -> 8080
az network lb rule update -g "rg-packer" --lb-name "vmss-lb" -n $1 --frontend-port "8080" --protocol "Tcp"