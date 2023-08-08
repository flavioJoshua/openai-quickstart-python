#!/bin/bash

while read -r line; do
  echo $line
  poetry add "$line"
done < requirements.toml.txt
echo $(date)
#!/bin/bash

while read -r line; do
  echo 
  poetry add ""
done < requirements.toml.txt
echo mar 8 ago 2023, 12:19:25, CEST
