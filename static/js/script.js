// // We'll save all chunks of audio in this array.
// const chunks = [];

// // We will set this to our MediaRecorder instance later.
// let recorder = null;

// // We'll save some html elements here once the page has loaded.
// let audioElement = null;
// let startButton = null;
// let stopButton = null;

// /**
//  * Save a new chunk of audio.
//  * @param  {MediaRecorderEvent} event 
//  */
// const saveChunkToRecording = (event) => {
//     chunks.push(event.data);
// };

// /**
//  * Save the recording as a data-url.
//  * @return {[type]}       [description]
//  */
// const saveRecording = () => {
//     const blob = new Blob(chunks, {
//         type: 'audio/mp4; codecs=opus'
//     });
//     const url = URL.createObjectURL(blob);

//     audioElement.setAttribute('src', url);
// };

// /**
//  * Start recording.
//  */
// const startRecording = () => {
//     recorder.start();
// };

// /**
//  * Stop recording.
//  */
// const stopRecording = () => {
//     recorder.stop();
// };


// // Wait until everything has loaded
// (function() {
//     audioElement = document.querySelector('.js-audio');
//     startButton = document.querySelector('.js-start');
//     stopButton = document.querySelector('.js-stop');
    
//     // We'll get the user's audio input here.
//     navigator.mediaDevices.getUserMedia({
//         audio: true // We are only interested in the audio
//     }).then(stream => {
//         // Create a new MediaRecorder instance, and provide the audio-stream.
//         recorder = new MediaRecorder(stream);

//         // Set the recorder's eventhandlers
//         recorder.ondataavailable = saveChunkToRecording;
//         recorder.onstop = saveRecording;
//     });

//     // Add event listeners to the start and stop button
//     startButton.addEventListener('mouseup', startRecording);
//     stopButton.addEventListener('mouseup', stopRecording);
// })();


// setTimeout(function(){
//     if ($('#msg').length > 0){
//         $('#msg').remove();
//     }
//     },2000);
