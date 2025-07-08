# #!/bin/bash

# create a post and get the ID
POST_RESPONSE=$(curl -s -X POST http://127.0.0.1:5000/api/timeline_post -d 'name=Random&email=random@email.com&content=This is a random message.')
echo "POST response: ${POST_RESPONSE}"

POST_ID=$(echo "$POST_RESPONSE" | jq '.id')
echo "Created post ID: $POST_ID"

# get all posts
curl -s -X GET http://127.0.0.1:5000/api/timeline_post | jq

# delete the post by id
curl -s -X DELETE http://127.0.0.1:5000/api/timeline_post/$POST_ID

# get all posts again to confirm deletion
curl -s -X GET http://127.0.0.1:5000/api/timeline_post | jq