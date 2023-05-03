
<div id="top"></div>

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <h3 align="center">Smart Classroom Assistant using AWS Lambda</h3>
  <p align="center">
     This assistant takes videos from the user’s classroom, performs face recognition on the collected videos, looks up the recognized students in the database, and returns the relevant academic information of each student back to the user. 
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#frameworks-and-tools-used">Frameworks And Tools Used</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#references">References</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

High level overview:
When users upload videos, it gets stored in the input bucket of S3. This triggers a Lambda function which processes the video.The lambda function uses a multimedia framework,ffmpeg, to extract frames from the video. The lambda then uses python face_recognition library to recognize faces from the frames. The first face it detects is classified and returned. The lambda function uses the name of the first recognized face to search in DynamoDB for this person's academic information.
<p align="right">(<a href="#top">go to top</a>)</p>

### Frameworks And Tools Used

* [Python](https://www.python.org/)
* [Boto3](https://aws.amazon.com/sdk-for-python/)

<p align="right">(<a href="#top">go to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

This section contains instructions on setting up the project locally.
To get a local copy up and running follow these simple steps.

There are two folders, Image recognition training & validation, and lambda 2 docker image.

To train the custom model, run

```
pip3 install -r install_requirements.txt
```

For training the model, we have to upload images of 160x160 resolution taken from the PI camera,
stored in real_images folder inside the training & validation folder. The images must follow the same
structure as the images in `test_me` directory.

```
python3 train_face_recognition.py –data_dir "data/real_images/" –num_epochs 100
```

For evaluating the model, run the command:
```
python3 eval_face_recognition.py –img_path “data/real_images/val/<name_of_student>/<name_of_file>.png”
```

For running the code in the first lambda function, directly copy the lambda_1.py file to the lambda
function code and deploy it.

For setting up the docker image for the second lambda function run:
```
docker build -t <folder_name> .
docker push <user_id><region>.amazonaws.com/<folder_name>:latest
```

For running the Raspberry PI script to push videos to S3, run:
```
pip3 install boto3
python3 push.py <time_in_minutes>
```

<p align="right">(<a href="#top">go to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.md` for more information.

<p align="right">(<a href="#top">go to top</a>)</p>

<!-- REFERENCES -->
## References

* [Choose an Open Source License](https://choosealicense.com)
* [AWS SDK for Python (boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

<p align="right">(<a href="#top">go to top</a>)</p>
