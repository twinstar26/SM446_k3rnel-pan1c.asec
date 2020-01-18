$(".query-form" ).submit(function(e) {
    e.preventDefault();
    if ($("#query").val() != "") {
        $(".add-queries").html($(".add-queries").html() + `
            <div class="alert alert-dark" role="alert">
                ${$("#query").val()}
            </div>
        `);
        let str = $("#query").val();
        $("#query").val("");

        $("#email").hide();
        $("#email").attr("disabled", false);
        $("#email").html("Send Via Email");
        $("#results").html("Loading....");

        $.post("/chatbot/", {
            user_query: str
        }, function(data, status) {
            if (status == "success") {
                $("#email").show();
                $("#results").html(data);
            } else {
                $("#results").html("Some Error Occured Please Try Again....");
            }
        });
    }
});

$("#email").on("click", (e) => {
    $("#email").attr("disabled", true);
    let content = $("#results").html();
    $.post("/email/", {
        content
    }, (data, status) => {
        $("#email").html("Sent");
    })
});

$("#stt").on("click", (e) => {
    navigator.mediaDevices.getUserMedia({ audio: true })
  .then(stream => {
    const mediaRecorder = new MediaRecorder(stream);
    mediaRecorder.start();
 
    const audioChunks = [];
    mediaRecorder.addEventListener("dataavailable", event => {
      audioChunks.push(event.data);
    });
 
    mediaRecorder.addEventListener("stop", () => {
      const audioBlob = new Blob(audioChunks, { 'type' : 'audio/wav;' });
      console.log(audioBlob);
      const audioUrl = URL.createObjectURL(audioBlob);
      const audio = new Audio(audioUrl);
    //   console.log(audio)
    //   audio.play();
        var formData = new FormData();
        formData.append('audio',audioBlob);
        formData.append('name',String('sound.wav'))

        // $.post("/stt/", {
        //     data: formData,
        //     processData: false,
        //     contentType: false,
        // }, (data, status) => {
        //     if (status == "success") {
        //         console.log(data);
        //     } else {
        //         console.log("Some Error Occured");
        //     }
        // })

        fetch('/stt/', {
             method: 'POST',
                body: formData
            })
            // .then(res => res.json())
            .then(data => {
                console.log(data)
            })
            .catch(err => console.log('err', err))
    });
 
    setTimeout(() => {
      mediaRecorder.stop();
    }, 5000);
  });

});

