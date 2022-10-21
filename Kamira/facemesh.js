
/*
const model = faceLandmarksDetection.SupportedModels.MediaPipeFaceMesh;
const detectorConfig = {
  runtime: 'mediapipe', // or 'tfjs'
  solutionPath: 'https://cdn.jsdelivr.net/npm/@mediapipe/face_mesh',
}
const detector = await faceLandmarksDetection.createDetector(model, detectorConfig);

const faces = await detector.estimateFaces(image);

[
    {
      box: {
        xMin: 304.6476503248806,
        xMax: 502.5079975897382,
        yMin: 102.16298762367356,
        yMax: 349.035215984403,
        width: 197.86034726485758,
        height: 246.87222836072945
      },
      keypoints: [
        {x: 406.53152857172876, y: 256.8054528661723, z: 10.2, name: "lips"},
        {x: 406.544237446397, y: 230.06933367750395, z: 8},
        
      ],
    }
  ]

  let predictions = [];
const video = document.getElementById('video');

// Create a new facemesh method
const facemesh = ml5.facemesh(video, modelLoaded);

// When the model is loaded
function modelLoaded() {
  console.log('Model Loaded!');
}

// Listen to new 'face' events
facemesh.on('face', results => {
  predictions = results;
});



const options = {
    flipHorizontal: false, // boolean value for if the video should be flipped, defaults to false
    maxContinuousChecks: 5, // How many frames to go without running the bounding box detector. Only relevant if maxFaces > 1. Defaults to 5.
    detectionConfidence: 0.9, // Threshold for discarding a prediction. Defaults to 0.9.
    maxFaces: 10, // The maximum number of faces detected in the input. Should be set to the minimum number for performance. Defaults to 10.
    scoreThreshold: 0.75, // A threshold for removing multiple (likely duplicate) detections based on a "non-maximum suppression" algorithm. Defaults to 0.75.
    iouThreshold: 0.3, // A float representing the threshold for deciding whether boxes overlap too much in non-maximum suppression. Must be between [0, 1]. Defaults to 0.3.
    }
    
    facemesh.predict(inputMedia, callback);

    facemesh.predict(inputMedia, results => {
        // do something with the results
        console.log(results);
      });

      [
    {
        faceInViewConfidence: 1, // The probability of a face being present.
        boundingBox: { // The bounding box surrounding the face.
            topLeft: [232.28, 145.26],
            bottomRight: [449.75, 308.36],
        },
        mesh: [ // The 3D coordinates of each facial landmark.
            [92.07, 119.49, -17.54],
            [91.97, 102.52, -30.54],
            
        ],
        scaledMesh: [ // The 3D coordinates of each facial landmark, normalized.
            [322.32, 297.58, -17.54],
            [322.18, 263.95, -30.54]
        ],
        annotations: { // Semantic groupings of the `scaledMesh` coordinates.
            silhouette: [
            [326.19, 124.72, -3.82],
            [351.06, 126.30, -3.00],
            
            ],
            
        }
    }
]

facemesh.on('face', callback);

facemesh.on('face', results => {
    // do something with the results
    console.log(results);
  });






Promise.all([
  faceapi.nets.tinyFaceDetector.loadFromUri('/models'),
  faceapi.nets.faceLandmark68Net.loadFromUri('/models'),
  faceapi.nets.faceRecognitionNet.loadFromUri('/models'),
  faceapi.nets.faceExpressionNet.loadFromUri('/models')
]).then(startVideo)

function startVideo() {
  navigator.getUserMedia(
    { video: {} },
    stream => video.srcObject = stream,
    err => console.error(err)
  )
}

video.addEventListener('play', () => {
  const canvas1 = faceapi.createCanvasFromMedia(video)
  document.body.append(canvas1)
  const displaySize = { width: video.width, height: video.height }
  faceapi.matchDimensions(canvas1, displaySize)
  setInterval(async () => {
    const detections = await faceapi.detectAllFaces(video, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()
    const resizedDetections = faceapi.resizeResults(detections, displaySize)
    canvas1.getContext('2d').clearRect(0, 0, canvas1.width, canvas1.height)
    faceapi.draw.drawFaceExpressions(canvas1, resizedDetections)
    /*
    faceapi.draw.drawDetections(canvas1, resizedDetections)
    faceapi.draw.drawFaceLandmarks(canvas1, resizedDetections)
  
}, 100)
})
  
*/