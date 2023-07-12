# import cv2
# import face_recognition
# import numpy as np
# import sqlite3

# # Connect to the database
# conn = sqlite3.connect('attendance.db')
# c = conn.cursor()

# # Create attendance table if it doesn't exist
# c.execute('''
#     CREATE TABLE IF NOT EXISTS attendance
#     (id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     date TEXT NOT NULL)
#     ''')

# # Load pre-trained face recognition models
# known_face_encodings = []
# known_face_names = []

# # Load known face encodings and names from the database
# c.execute("SELECT name, encoding FROM users")
# rows = c.fetchall()
# for row in rows:
#     known_face_names.append(row[0])
#     known_face_encodings.append(np.frombuffer(row[1]))

# # Initialize webcam
# video_capture = cv2.VideoCapture(0)

# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()

#     # Convert the image from BGR color (OpenCV) to RGB color (face_recognition)
#     rgb_frame = frame[:, :, ::-1]

#     # Find all the faces and their encodings in the current frame
#     face_locations = face_recognition.face_locations(rgb_frame)
#     face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

#     # Initialize an array for storing names of detected faces
#     face_names = []

#     for face_encoding in face_encodings:
#         # Compare the detected face with known faces
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         name = "Unknown"

#         # Find the best match and assign the name
#         if True in matches:
#             first_match_index = matches.index(True)
#             name = known_face_names[first_match_index]

#             # Insert attendance data into the database
#             c.execute("SELECT * FROM attendance WHERE name = ? AND date = ?", (name, date))
#             result = c.fetchall()
#             if len(result) == 0:
#                 c.execute("INSERT INTO attendance (name, date) VALUES (?, ?)", (name, date))
#                 conn.commit()

#         face_names.append(name)

#     # Display the results
#     for (top, right, bottom, left), name in zip(face_locations, face_names):
#         cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
#         cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

#     # Display the resulting image
#     cv2.imshow('Face Recognition', frame)

#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the webcam and close all windows
# video_capture.release()
# cv2.destroyAllWindows()
