echo "##################################################################"
echo "################     Enter Commit Tag           ##################"
echo "##################################################################"
git remote -v
git add --all .


read input
git commit -m '$input'
git push -u origin master
