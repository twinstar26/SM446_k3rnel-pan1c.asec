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
        console.log("Data: " + data + "\nStatus: " + status);
    });
});

