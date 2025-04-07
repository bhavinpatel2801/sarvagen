import requests

url = "https://dl.fbaipublicfiles.com/segment_anything/sam_vit_b.pth"
response = requests.get(url)
with open("checkpoints/sam_vit_b.pth", "wb") as f:
    f.write(response.content)
