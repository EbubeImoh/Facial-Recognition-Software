from deepface import DeepFace
result = DeepFace.verify("reference2.jpg", "reference.jpg")

print("Is verified: ", result["verified"])