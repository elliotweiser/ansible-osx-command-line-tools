#!/bin/bash

set -e

PLATFORM=${PLATFORM:=sierra}
BOX_NAME=macosx-${PLATFORM}-clt
PROVIDER=${PROVIDER:=virtualbox}
if [ -z "${VERSION}" ]; then
  echo "VERSION is unset" 1>&2
fi
echo PLATFORM=${PLATFORM}
echo BOX_NAME=${BOX_NAME}
echo PROVIDER=${PROVIDER}
echo VERSION=${VERSION}

molecule destroy
molecule converge --platform=${PLATFORM}
molecule verify --platform=${PLATFORM}

ln -sf "$(git rev-parse --show-toplevel)/.molecule/vagrantfile" Vagrantfile
vagrant package --output ${BOX_NAME}.box macosx-${PLATFORM}
rm -f Vagrantfile

ansible-vault decrypt --vault-password-file=.ansible_vault_password vault
ACCESS_TOKEN=$(cat vault | jq -r '.atlas_token')
ansible-vault encrypt --vault-password-file=.ansible_vault_password vault

BASE_URL='https://atlas.hashicorp.com/api/v1/box/elliotweiser'
BOX_PARAMS="${BOX_NAME}/version/${VERSION}/provider/${PROVIDER}"
FULL_URL="${BASE_URL}/${BOX_PARAMS}/upload?access_token=${ACCESS_TOKEN}"
curl -X PUT -T ${BOX_NAME}.box $(curl "${FULL_URL}" | jq -r '.upload_path')
