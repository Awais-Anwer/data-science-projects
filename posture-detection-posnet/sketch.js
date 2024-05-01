let capture;
let posenet;
let singlepose, skeleton;

function setup(){   // setup related code -> run for ones    
    createCanvas(800, 500);
    capture = createCapture(VIDEO);
    capture.hide();

    posenet = ml5.poseNet(capture, modelLoaded);
    posenet.on('pose', receivedPoses)

}

function receivedPoses(poses){
    console.log(poses);

    if(poses.length > 0){
        singlepose = poses[0].pose;
        skeleton = poses[0].skeleton;
    }
}

function modelLoaded(){
    console.log("Model has loaded")
}

function draw(){  // draw things -> runs in loop

    // images and videos(webcam)
    image(capture, 0, 0);
    fill(255, 0, 0)
    
    if(singlepose){
        for(let i=0; i<singlepose.keypoints.length; i++){
            ellipse(singlepose.keypoints[i].position.x, singlepose.keypoints[i].position.y, 15);
        }
    }

    stroke(255, 255, 255);
    strokeWeight(5);
    if(skeleton){
        for(let i=0; i<skeleton.length; i++){
            line(skeleton[i][0].position.x, skeleton[i][0].position.y, skeleton[i][1].position.x, skeleton[i][1].position.y);
        }
    }
}