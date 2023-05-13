
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

