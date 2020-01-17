$('#content-area').height($(window).height()-50)
$('#chat-area').height($(window).height()-50)
$('#chat').height($(window).height()-90)

$(document).ready(function(){
    $('#query').keypress(function(e){
        // console.log("helllo1")
        if(e.keyCode==13){
            // console.log("he;llo")
            let queryValue = document.querySelector("#query").value
            if(queryValue==""){}
            else{
                let chatHtml = document.querySelector("#chat").innerHTML
                chatHtml += `<div class="left-text">
                            <p class="text">` +
                                queryValue
                            + `</p>
                        </div>`
                document.querySelector("#chat").innerHTML = chatHtml
                document.querySelector("#query").value = ""
                let formData = { "user_query": queryValue}
                $.ajax({
                    url : "http://localhost:5000/",
                    type: "POST",
                    cors:true,
                    data : formData,
                    success: function(data, textStatus, jqXHR){
                        //data - response from server
                        console.log("data : " + data)
                        // $("#h11").html(data); 
                    },
                    error: function (jqXHR, textStatus, errorThrown){
                        console.log('error')
                    }
            });
            $.ajax({
                url : "http://localhost:5000/",
                type: "GET",
                cors:true,
                // data : formData,
                success: function(data, textStatus, jqXHR){
                    //data - response from server
                    console.log("data : " + data)
                    // $("#h11").html(data); 
                },
                error: function (jqXHR, textStatus, errorThrown){
                    console.log('error')
                }
        });
        // fetch('https://localhost:5000')
        // .then((response) => {
        //     return response.json();
        // })
        // .then((myJson) => {
        //     console.log(myJson);
        // });

            }
        }
    });
});

// let button;
// let mic;
// let soundRec;
// let soundFile;


// // function setup() {
//   mic = new p5.AudioIn();
//   mic.start();
//   soundRec = new p5.SoundRecorder();
//   soundRec.setInput(mic)
//   soundFile = new p5.SoundFile();

// //   button = createDiv("");
// //   button.position(100,100);
// //   button.size(100,100);
// //   button.style('background-color', 'grey');


//   document.querySelector("#mic-btn").addEventListener("click",(mouseEvent)=>{
//     console.log("recording....");
//     soundRec.record(soundFile); // set up the soundfile to record and start recording

//     let recordingTimer = setTimeout(()=>{ // setup a timeout for the recording, after the time below expires, do the tings inside the {}    

//       soundRec.stop(); // stop recording
//       let soundBlob = soundFile.getBlob(); //get the recorded soundFile's blob & store it in a variable

//       let formdata = new FormData() ; //create a from to of data to upload to the server
//       formdata.append('soundBlob', soundBlob,  'myfiletosave.wav') ; // append the sound blob and the name of the file. third argument will show up on the server as req.file.originalname

//           // Now we can send the blob to a server...
//       var serverUrl = '/upload'; //we've made a POST endpoint on the server at /upload
//       //build a HTTP POST request
//       var httpRequestOptions = {
//         method: 'POST',
//         body: formdata , // with our form data packaged above
//         headers: new Headers({
//           'enctype': 'multipart/form-data' // the enctype is important to work with multer on the server
//         })
//       };
//       // console.log(httpRequestOptions);
//       // use p5 to make the POST request at our URL and with our options
//       httpDo(
//         serverUrl,
//         httpRequestOptions,
//         (successStatusCode)=>{ //if we were successful...
//           console.log("uploaded recording successfully: " + successStatusCode)
//         },
//         (error)=>{console.error(error);}
//       )
//       console.log('recording stopped');

//     },20000) //record for one second

//   }) // close mouseClicked handler


// // } //close setup()