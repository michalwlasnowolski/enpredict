$(document).ready(function(){

    $("#selectall").change('click', function(){
        if($(this).is(':checked')) {
        $(".chkbox").prop('checked', true).change();
        $(".one_chromosome").prop('checked', true).change();
        }
        else {
     $(".chkbox").prop('checked', false).change();
     $(".one_chromosome").prop('checked', false).change();
        }
    });


    $(".one_chromosome").change('click', function(){

        if($(this).is(':checked')) {
        $("."+this.id).prop('checked', true).change();
        }
        else {
     $("."+this.id).prop('checked', false).change();
        }
    });

});
