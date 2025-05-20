#!/bin/bash

for dir in */ ; do
  echo "👉 Entering directory: $dir"
  cd "$dir" || continue

  echo "🔍 Running terraform plan in $dir"
  terraform init -input=false
  terraform plan

  #echo "🚀 Applying terraform in $dir"
  #terraform apply -auto-approve

  echo "⬅️ Exiting directory: $dir"
  cd ..
done

