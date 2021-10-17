function rate(sourceElem, rating, resourceID, rateType) {
    $(sourceElem).html(rating);
    $.post('/rate_resource', {
        resource_id: resourceID,
        rating: rating,
        rate_type: rateType
    }).done(function(response) {
        console.log("Sucessfuly rated the resource.");
    }).fail(function() {
        console.log("'Error: Could not save resource.'");
    });
};