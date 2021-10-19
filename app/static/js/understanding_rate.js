function understanding_rate(sourceElem, rating) {
    $(sourceElem).html(rating);
};

function get_understanding(sourceElem, chosenLevel, resourceID1, resourceID2, resourceID3) {
    $.post('/evaluate/get_understanding', {
        chosenLevel: chosenLevel,
        understanding1: $(resourceID1).val(),
        understanding2: $(resourceID2).val(),
        understanding3: $(resourceID3).val()
    }).done(function(response) {
        level = response['level']
        $(sourceElem).html(level);
    }).fail(function() {
        console.log("'Error: Could not save resource.'");
    });
}