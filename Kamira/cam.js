let canvas = document.querySelector("#canvas");
let context = canvas.getContext("2d");
let video = document.querySelector("#video");
//let canvas1 = document.querySelector("#ctx");
let capture = document.querySelector("snap")


if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
  navigator.mediaDevices.getUserMedia({video: true}).then((stream) => {
    video.srcObject = stream;
   video.play();

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
        document.getElementById('snap').addEventListener('click', ()=> {
          context.drawImage(video, 0, 0, 640, 480 );
          })
      }
    }); 
  }  

     

     // video.addEventListener('play', () => {
       // console.log(video)
       // const context = faceapi.createCanvasFromMedia(video)
       // document.body.append(context)
        //const displaySize = { width: context.width, height: context.height }
        //faceapi.matchDimensions(context, displaySize)
        
     //setInterval(async () => {
         // const detections = await faceapi.detectAllFaces(context, new faceapi.TinyFaceDetectorOptions()).withFaceLandmarks().withFaceExpressions()
          //const resizedDetections = faceapi.resizeResults(detections, displaySize)
         // canvas.getContext('2d').clearRect(0, 0, context.width, context.height)
          //faceapi.draw.drawFaceExpressions(context, resizedDetections)
          
          //faceapi.draw.drawDetections(canvas1, resizedDetections)
          //faceapi.draw.drawFaceLandmarks(canvas1, resizedDetections)
        
      //}, 100)
     // })
        


//document.getElementById('snap').addEventListener('click', ()=> {
//context.drawImage(video, 0, 0, 640, 480);
//})



/* Splash */

let intro = document.querySelector('.Intro');
let logo = document.querySelector('.logo-header');
let logoSpan = document.querySelectorAll('.logo');

window.addEventListener('DOMContentLoaded', () =>{

    setTimeout(() =>{

logoSpan.forEach((span, idx) =>{
    setTimeout(()=>{
        span.classList.add('active');
}, (idx + 1) * 400)
}, 500000);

setTimeout(() =>{
    logoSpan.forEach((span, idx) =>{

        setTimeout(()=>{
            span.classList.add('active');
            span.classList.add('fade');
    }, (idx + 1) * 10)
    })
} , 500000);

setTimeout(()=>{
    intro.style.top = '-100vh';
},4500)

})

})



