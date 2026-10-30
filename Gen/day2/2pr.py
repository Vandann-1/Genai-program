

import os

base_url = os.getenv(
    "BASE_URL",
    "https://jsonplaceholder.typicode.com/posts/3"
    
    )

print(base_url)