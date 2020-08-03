//webkitURL is deprecated but nevertheless
URL = window.URL || window.webkitURL;

var gumStream; 						//stream from getUserMedia()
var rec; 							//Recorder.js object
var input; 							//MediaStreamAudioSourceNode we'll be recording

// shim for AudioContext when it's not avb.
var AudioContext = window.AudioContext || window.webkitAudioContext;
var audioContext //audio context to help us record

var button = document.getElementById("mic");

//add events to those 2 buttons
button.addEventListener("click", startRecording);

function startRecording() {
	console.log("recordButton clicked");

	/*
		Simple constraints object, for more advanced audio features see
		https://addpipe.com/blog/audio-constraints-getusermedia/
	*/

	var constraints = { audio: true, video:false }
	button.removeEventListener("click", startRecording);
	button.addEventListener("click", stopRecording);
	button.innerHTML = "<i class='fa fa-stop' style='font-size: 10rem;'></i>";
 	/*
    	Disable the record button until we get a success or fail from getUserMedia()
	*/

	/*
    	We're using the standard promise based getUserMedia()
    	https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia
	*/

	navigator.mediaDevices.getUserMedia(constraints).then(function(stream) {
		console.log("getUserMedia() success, stream created, initializing Recorder.js ...");

		/*
			create an audio context after getUserMedia is called
			sampleRate might change after getUserMedia is called, like it does on macOS when recording through AirPods
			the sampleRate defaults to the one set in your OS for your playback device

		*/
		audioContext = new AudioContext();

		//update the format
		// document.getElementById("formats").innerHTML="Format: 1 channel pcm @ "+audioContext.sampleRate/1000+"kHz"

		/*  assign to gumStream for later use  */
		gumStream = stream;

		/* use the stream */
		input = audioContext.createMediaStreamSource(stream);

		/*
			Create the Recorder object and configure to record mono sound (1 channel)
			Recording 2 channels  will double the file size
		*/
		rec = new Recorder(input,{numChannels:1})

		//start the recording process
		rec.record()

		console.log("Recording started");

	}).catch(function(err) {
		//enable the record button if getUserMedia() fails
		button.addEventListener("click", startRecording);
	});
}

function stopRecording() {
	console.log("stopButton clicked");

	//reset button just in case the recording is stopped while paused

	//tell the recorder to stop the recording
	rec.stop();

	//stop microphone access
	gumStream.getAudioTracks()[0].stop();

	//create the wav blob and pass it on to createDownloadLink
	rec.exportWAV(createDownloadLink);
	button.removeEventListener("click", stopRecording);
	button.addEventListener("click", startRecording);
	button.innerHTML="<i class='fa fa-microphone' style='font-size: 10rem;'></i>";
}

function createDownloadLink(blob) {
	var filename = new Date().toISOString();

	var xhr=new XMLHttpRequest();
	xhr.onload=function(e) {
		if(this.readyState === 4) {
			console.log("Server returned: ",e.target.responseText);
		}
	};
	var fd=new FormData();
	fd.append("audio_data",blob, filename);
	xhr.onreadystatechange = function() {
		if (xhr.readyState === 4) {
			$("#email").show();
			console.log('hello hello')
			$(".add-queries").html($(".add-queries").html() + `
				<div class="alert alert-dark" role="alert">
					${xhr.responseText.split("|")[0]}
				</div>
			`);
			$("#results").html(xhr.responseText.split("|")[1]);
		} else {
			$("#results").html("Loading....");
		}
	}
	xhr.open("POST","/mom/",true);
	xhr.send(fd);
}