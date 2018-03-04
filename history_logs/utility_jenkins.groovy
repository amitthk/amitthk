def performFullBuild(String timeStamp, String project_id,String deploy_env, String npmHome){

stage('Clean'){

sh 'rm -rf dist && rm -rf dist.tar.gz && rm -rf release/*.tar.gz'

}

stage('Get Dependencies'){

withEnv(["PATH+NODE=${npmHome}/bin","NODE_HOME=${npmHome}"]) {

sh "npm install --max-old-space-size=200"

}

}

stage('Code Analysis'){

try{

withEnv(["PATH+NODE=${npmHome}/bin","NODE_HOME=${npmHome}"]) {

sh '$npm run lint'

}

}catch(err){

echo 'Code Quality Analysis failed!'

}

}

stage('Build'){

withEnv(["PATH+NODE=${npmHome}/bin","NODE_HOME=${npmHome}"]) {

sh "npm run build -- --prod --environment=${deploy_env} --max-old-space-size=200"

}

}

stage('Archive')

{

sh 'mkdir -p release'

sh "cd dist && tar -czvf ../release/${project_id}-${timeStamp}.tar.gz . && cd .."

stash includes: 'release/*.tar.gz', name: "${project_id}"

stash includes: 'dist/**/*', name: "${project_id}_dist"

}

}



def isFileAffected(String match) {

def changeLogSets = currentBuild.changeSets;

def filesAffected = [];

for (int i = 0; i < changeLogSets.size(); i++) {

def entries = changeLogSets[i].items

for (int j = 0; j < entries.length; j++) {

def entry = entries[j];

def files = new ArrayList(entry.affectedFiles);

for(int k =0; k < files.size(); k++){

if(files[k] == match){

return true;

}

}

}

}

return false;

}



def notifyJobStatus(int notificationQueueId, String message){

def notificationTimeStamp=getTimeStamp();

statusJson = "{\"id\": ${notificationQueueId}, \"createdOn\": ${notificationTimeStamp}, \"notificationMessage\": \"${message}\"}";

sendNotification(statusJson);

}



def sendNotification(String statusJson) {

def command = "curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '${statusJson}' 'dev.myapp.com/notifications/notify'";

sh command;

}