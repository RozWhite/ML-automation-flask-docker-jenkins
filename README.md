# Automation of Machine Learning with Jenkins and Docker 
The purpose of this project is building and automating a Machine Learning pipelines with DevOps tools like Docker and Jenkins. This is an End-to-End ML application with Flask REST API, Flasgger and Docker which build Jenkins job automatically on GitHub Commit.</br></br>

<img src="images/pipeline.png"  height="400"/>

## Project Structure
This project has the following steps:
1.	Building  Machine Learning Model with Logistic Regression
2.	Deploying Machine Learning Model with Flask API and Flasgger 
3.	Containerize Machine Learning Model with Docker
4.	Automating Machine Learning pipeline with Jenkins and GitHub 

## 1.	Building  Machine Learning
In this step I used Logistic Regression model to to classify iris species. The Iris dataset can be download from scikit-learn which consists of 3 different types of irises' (Setosa, Versicolour, and Virginicapes). The output of the iris.py will be validation accuracy  and test accuracy as json file and a Pickle file to the machine learning model.

## 2.	Deploying Machine Learning Model
Flask is a framework to create APIs in Python and Flasgger helps to create a simple Frontend for ML application.

### To run the application locally:
Run: python app.py 

Test the API at <http://localhost:3000/apidocs/>


## 3.	Containerize Machine Learning Model with Docker

You can use the docker file from here or just download the existing image from [DockerHub](https://hub.docker.com/r/rozitadocker123/ml_flask_docker/).
```
docker pull rozitadocker123/ml_flask_docker
```

To build the Docker image :
```
docker image build -t iris_docker . 
```

To run the Docker image:
```
docker run -d --name iris_model --rm -p 3000:3000 iris_docker
```
You can then test the API at <http://localhost:3000/apidocs/>  within the docker</br>


To run commands inside the container:
```
docker container exec iris_model python3 iris.py
```

To read the model validation accuracy  and test accuracy:
```
docker container exec iris_model cat  ./train_metadata.json ./test_metadata.json
```

## 4.	Automating Machine Learning pipeline with Jenkins and GitHub 

### Jenkins GitHub Integration with Webhook
To integrate jenkins with Github, jenkins must have a public IP, I used Ngrok to convert localhost to a public web address. Under your repository name, click Settings and select webhooks. In the Payload URL, pass the jenkins public URL and add ???//github-webhook/???. Fill in the remaining part as shown in the figure below.</br></br> 

<img src="images/webhook.png"  width="600"/></br>

The next step is to create a credential in Jenkins to access GitHub. Under the ???Manage Jenkins??? select ???Manage Credentials??? . In ???Stores scoped to Jenkins??? Add credentials.

### Build the Jenkins Jobs
#### JOB #1:
The first job the first Job will automatically pull repo from the GitHub Repo just by giving some triggers and then building a Docker image. In the Jenkins Dashboard, click the New Item, give it a name, and select Freestyle Project. In the Build Section, if there is a Docker container available, we need to delete it  then build a new Docker image and container.</br>

```
docker rm -f iris_model
docker image build -t iris_docker . 
docker run -d --name iris_model --rm -p 3000:3000 iris_docker
``` 
<img src="images/Job1.png"  width="600"/></br>

#### JOB #2:
This job is triggered after the first job is completed. Therefore, in the "Build Triggers" section, we need to select the "Build after other projects are built" option.Here we execute commands inside the container created by Job 1 and read the model validation accuracy and test accuracy.</br></br> 
<img src="images/Job2.png"  width="600"/></br>

### Console Output of Job2:
<img src="images/console.JPG"  width="600"/></br>

You can then test the API at <http://localhost:3000/apidocs/></br></br>
<img src="images/UI.JPG"  width="600"/></br>

### New Commit:
Try to do a commit in GitHub and see how each step runs automatically. 