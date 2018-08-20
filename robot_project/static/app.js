$(document).ready(function() {

    $('.deleteButton').on('click', function() {

        var robot_id = $(this).attr('robot_id');

        if (confirm('Do you really want to delete this robot?')) {

        req = $.ajax({
            url : '/robots/delete',
            type : 'POST',
            data : { robot_id : robot_id }
        });

        req.done(function(data) {

           $("#robotId"+data.robot_id).remove();

        });

    };

    });

});
