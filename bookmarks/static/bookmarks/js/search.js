



function search_submit() {
    var query = $("#id_query").val();
    $("#search-results").load(
        "/bookmarks/search/?ajax&query=" + encodeURIComponent(query)
        );
        return false;
    }
$(document).ready(function () {
    $("#search-form").submit(search_submit);

    });
