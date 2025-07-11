curl --request POST http://localhost:5001/api/timeline_post -d 'name=Lucas&email=l47kim@uwaterloo.com&content=Added a MySQL database' > /dev/null 2>&1

RESULT=$(curl http://localhost:5001/api/timeline_post 2>"/dev/null")

if [[ "$RESULT" =~ "Added a MySQL database" ]]
then
  echo "SUCCESS: Post added successfully"
else
  echo "FAIL: Post not added"
fi