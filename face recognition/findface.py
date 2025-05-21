import face_recognition



ref_img=["elon musk.jpg","gandhi ji.jpg","jeff bezos.jpg","MESSI.jpg","ryan reynolds.jpg","me.jpg"]
ref_encodings=[]

for x in ref_img:
    image=face_recognition.load_image_file(x)
    en=face_recognition.face_encodings(image)[0]
    ref_encodings.append(en)

counter=0
mudit=face_recognition.load_image_file("C:\\Users\\Mudit\\Desktop\\face recognition\\me.jpg")
mudit_encoded=face_recognition.face_encodings(mudit)[0]

for i in ref_img:
    img=face_recognition.load_image_file(i)
    img_encoded=face_recognition.face_encodings(img)[0]

    results=face_recognition.compare_faces([img_encoded],mudit_encoded)

    if results[0]:
        counter=counter+1
        
    else:
        print("match not found!")
        
print(f"found{counter}matches!")