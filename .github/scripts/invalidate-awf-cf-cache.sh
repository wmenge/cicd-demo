#!/bin/bash

id=$(aws cloudfront create-invalidation --distribution-id=$1 --paths='/*' | jq -r .Invalidation.Id)

echo $id

aws cloudfront wait invalidation-completed --id $id --distribution-id $1
