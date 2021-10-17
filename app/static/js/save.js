function save(sourceElem, resourceID, imageURL) {
    $(sourceElem).html('<img src="imageURL">');
    $.post('/save_resource', {
        resource_id: resourceID
    }).done(function(response) {
        $(sourceElem).html('saved')
    }).fail(function() {
        $(sourceElem).text("'Error: Could not save resource.'");
    });
};