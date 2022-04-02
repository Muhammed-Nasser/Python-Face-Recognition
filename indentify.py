import face_recognition
from PIL import Image, ImageDraw

image_of_mohamed = face_recognition.load_image_file('./img/known/mohamed nasser.jpg')
mohamed_face_encoding = face_recognition.face_encodings(image_of_mohamed)[0]

#  Create arrays of encodings and names
known_face_encodings = [
  mohamed_face_encoding,
]

known_face_names = [
  "Muhammad Nasser",
]

# Load test image to find faces in
test_image = face_recognition.load_image_file('./img/groups/group-image.jpg')

# Find faces in test image
face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

# Convert to PIL format
mohamed_image = Image.fromarray(test_image)

# Create a ImageDraw instance
draw = ImageDraw.Draw(mohamed_image)

# Loop through faces in test image
for(top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
  matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

  name = "Unknown Person"

  # If match
  if True in matches:
    first_match_index = matches.index(True)
    name = known_face_names[first_match_index]
  
  # Draw box
  draw.rectangle(((left, top), (right, bottom)), outline=(255,255,0))

  # Draw label
  text_width, text_height = draw.textsize(name)
  draw.rectangle(((left,bottom - text_height - 10), (right, bottom)), fill=(255,255,0), outline=(255,255,0))
  draw.text((left + 6, bottom - text_height - 5), name, fill=(0,0,0))

del draw

# Display image
mohamed_image.show()

# Save image
mohamed_image.save('identify.jpg')