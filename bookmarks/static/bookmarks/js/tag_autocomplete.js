$(document).ready(function () {
    $("#id_tags").autocomplete(
       'bookmarks/ajax/tag/autocomplete/',{ multiple: true,multipleSeparator: ' '}
       ) ;
    });