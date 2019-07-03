git remote -v
git add --all .

echo "##################################################################"
echo "################     Enter Commit Tag           ##################"
echo "##################################################################"
read input
git commit -m '$input'
git push -u origin master
