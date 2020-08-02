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
    console.log(content)
    $.post("/email/", {
        content: content
    }, (data, status) => {
        $("#email").html("Sent");
    })
});