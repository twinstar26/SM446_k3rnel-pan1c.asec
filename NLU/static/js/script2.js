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

        $("#results").html("Loading....");

        $.post("/chatbot/", {
            user_query: str
        }, function(data, status) {
            if (status == "success") {
                $("#results").html(data);
            } else {
                $("#results").html("Some Error Occured Please Try Again....");
            }
        });
    }
});