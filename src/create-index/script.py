import pickle
with open("image_paths.pkl", 'rb') as f:
    image_paths = pickle.load(f)

print(list(image_paths)[:10])
