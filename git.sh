if git remote != origin ; then
  echo "Enter Your Repo Name"
  read repo
  git  remote add origin https://github.com/thavanix/$repo
fi

git remote -v
git add --all .

echo "##################################################################"
echo "################     Enter Commit Tag           ##################"
echo "##################################################################"
read input
git commit -m $input
git push -u origin master
