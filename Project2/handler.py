import pickle,boto3,os,face_recognition
from boto3.dynamodb.conditions import Attr
import csv

#Bucket names
input_bucket = "cse546-input-project2"
output_bucket = "output-project2-cse546"

s3 = boto3.client('s3')

# Function to read the 'encoding' file
def open_encoding(filename):
	file = open(filename, "rb")
	data = pickle.load(file)
	file.close()
	return data

def face_recognition_handler(event, context):	
	print("Hello", event)

	#Download the video file 
	video_name = event['Records'][0]['s3']['object']['key']
	video_path = '/tmp/'+video_name
	s3.download_file('cse546-input-project2', video_name, video_path)
	print("downloaded")
	
	#Run ffmpeg to extract the frames
	#/usr/bin/ffmpeg -i /home/app/test_8.mp4 -r 1 /tmp/images/image3.jpeg
	imgpath = '/tmp/'
	cmd = "/usr/bin/ffmpeg -i " + video_path + " -r 1 " + imgpath + "image-%3d.jpeg" 
	os.system(cmd)
	print("frames extracted")

	#Get the name of the person using the face_recognition package
	#Get encoding of extracted frames 
	encodings = open_encoding("encoding")
	print(os.listdir("/tmp"))

	for i in os.listdir("/tmp"):
		if ".jpeg" in i:
			frame=face_recognition.load_image_file("/tmp/"+i)
			face_locations=face_recognition.face_locations(frame)
			print("face_locations",face_locations)
			if len(face_locations)>0:
				print("face detected in image")
				break
	
	test_encoding = face_recognition.face_encodings(frame)[0]
	index = 0
	for enc in encodings['encoding']:
		if(face_recognition.compare_faces([enc],test_encoding)[0]):
			break
		index = index+1
	
	student_name = encodings['name'][index]
	print("student_name",student_name)

	#Search DynamoDB by student_name and get the student details
	dynamodb = boto3.resource('dynamodb', region_name='us-east-1',endpoint_url='https://dynamodb.us-east-1.amazonaws.com')
	DYNAMO_TABLE_NAME = 'project2'
	table = dynamodb.Table(DYNAMO_TABLE_NAME)
	response = table.scan(
    FilterExpression=Attr('name').eq(student_name)
)
	print(response['Items'][0])
	record=response['Items'][0]

	# send output as csv to s3 bucket.
	fields = ['Name', 'Major', 'Year']
	rows = [ [record['name'],record['major'],record['year']] ]
	filename = "/tmp/"+video_name[:-4]+".csv"
	with open(filename, 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(fields)
		csvwriter.writerows(rows)
	s3.upload_file(filename, output_bucket, video_name[:-4])

	print("Uploaded to s3, Byeee....")


