$(function(){
    $('#save_button').click(function(){
        $('#person_form').ajaxSubmit({dataType : 'json', success: function(o) {
            $('.error').empty();
            if(o === 1)
                $('#form_state').html('Person was successfully updated');
            else
                if(typeof(o.errors) != undefined)
                    for(i in o.errors)
                        $('#' + i + '_error').html(i + ':: ' +o.errors[i][0]);    
        }}); 
    });
    
    $('#person_form').keypress(function(e) {
        if(e.keyCode == 13)
            $('#save_button').trigger('click');
    });

});
