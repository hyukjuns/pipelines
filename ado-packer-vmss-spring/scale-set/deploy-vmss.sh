#!/bin/bash

# $1: GREEN 서브넷
# $2: Build Pipeline의 Build Number, 시스템변수
# $3: GREEN 백앤드풀

# create vmss with new image
az vmss create \
-n "new-vmss" \
-g "rg-packer" \
--load-balancer "vmss-lb" \
--vnet-name "vmss-vnet" \
--subnet $1 \
--image "springboot-application-$2" \
--vm-sku "Standard_A2_v2" \
--admin-username  <USERNAME> \
--admin-password <PASSWORD> \
--backend-pool-name $3 \
--upgrade-policy-mode "Automatic" \
--instance-count 2