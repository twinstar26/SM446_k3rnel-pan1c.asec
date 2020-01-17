$(".query-form" ).submit(function(e) {
    e.preventDefault();
    $(".add-queries").html($(".add-queries").html() + `
        <div class="alert alert-dark" role="alert">
            ${$("#query").val()}
        </div>
    `);
    let str = $("#query").val();
    $("#query").val("");

    $.post("/chatbot/", {
        user_query: str
    }, function(data, status) {
        if (status == "success") {
            $("#results").html(data);
        } else {
            $("#results").html("Some Error Occured Please Try Again...."); 
        }
    });
});

$("#stt").on("click", (e) => {
    e.preventDefault();
    
})