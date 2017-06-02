"""
source: https://gist.github.com/deekayen/4148741
"""
with open('eng100.txt') as f:
    output=""
    for line in f:
        output+= "'"+ line.strip() + "',"
print output